# app/scripts/load_real_data.py
import requests
from sqlmodel import Session
from app.db import engine
from app.models import Product

API_URL = "https://world.openfoodfacts.org/api/v2/search"
COUNTRY = "chile"
CATEGORY = "food"
PAGE_SIZE = 100  # cantidad de productos por página
TOTAL_PAGES = 5  # cuántas páginas quieres descargar

def fetch_products():
    products = []
    for page in range(1, TOTAL_PAGES + 1):
        params = {
            "countries": COUNTRY,
            "categories": CATEGORY,
            "page": page,
            "page_size": PAGE_SIZE,
        }
        print(f"📦 Descargando página {page}...")
        resp = requests.get(API_URL, params=params, timeout=10)
        if resp.status_code != 200:
            print(f"⚠️ Error al descargar la página {page}: {resp.status_code}")
            continue
        data = resp.json()
        products.extend(data.get("products", []))
    print(f"✅ Total productos descargados: {len(products)}")
    return products

def normalize_product(p: dict):
    """
    Convierte los datos de OpenFoodFacts al modelo Product
    """
    barcode = p.get("code")
    if not barcode:
        return None
    name = p.get("product_name") or p.get("generic_name") or "Desconocido"
    brand = (p.get("brands") or "").split(",")[0] if p.get("brands") else None
    category = None
    if p.get("categories_tags"):
        category = p["categories_tags"][0].split(":")[-1]  # toma la primera categoría
    price = None  # no disponible en OF
    weight_kg = None
    if "quantity" in p:
        qty = p["quantity"]
        # intento simple: si termina en g, convertir a kg
        if "g" in qty.lower():
            try:
                weight_kg = float(qty.lower().replace("g", "").strip()) / 1000
            except:
                weight_kg = None
        elif "kg" in qty.lower():
            try:
                weight_kg = float(qty.lower().replace("kg", "").strip())
            except:
                weight_kg = None
    packaging = p.get("packaging")
    estimated_carbon = None  # no disponible en OF
    return Product(
        barcode=barcode,
        name=name,
        brand=brand,
        category=category,
        price=price,
        weight_kg=weight_kg,
        packaging=packaging,
        estimated_carbon=estimated_carbon,
    )

def load_real_data():
    products_raw = fetch_products()
    products = [normalize_product(p) for p in products_raw]
    products = [p for p in products if p is not None]

    with Session(engine) as session:
        for p in products:
            # evitar duplicados
            existing = session.get(Product, p.barcode)
            if not existing:
                session.add(p)
        session.commit()
    print(f"✅ {len(products)} productos guardados en la base de datos")

if __name__ == "__main__":
    load_real_data()
