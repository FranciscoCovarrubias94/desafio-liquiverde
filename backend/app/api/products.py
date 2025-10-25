from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select
from app.db import get_session
from app.models import Product
from app.schemas import ProductCreate
import requests

router = APIRouter()

OPENFOOD_URL = "https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

@router.get("/product/{barcode}")
def get_product(barcode: str, session = Depends(get_session)):
    statement = select(Product).where(Product.barcode == barcode)
    result = session.exec(statement).first()
    if result:
        return result
    try:
        r = requests.get(OPENFOOD_URL.format(barcode=barcode), timeout=5)
    except Exception:
        raise HTTPException(status_code=502, detail="External API error")
    if r.status_code != 200:
        raise HTTPException(status_code=404, detail="Not Found")
    data = r.json()
    if data.get("status") != 1:
        raise HTTPException(status_code=404, detail="Not Found")
    p = data.get("product", {})
    name = p.get("product_name") or p.get("generic_name") or "Desconocido"
    brand = (p.get("brands") or "").split(",")[0] if p.get("brands") else None
    image_url = p.get("image_front_small_url") or p.get("image_url")
    category = None
    if p.get("categories"):
        category = p.get("categories").split(",")[0].strip()
    product = Product(
        barcode=barcode,
        name=name,
        brand=brand,
        category=category,
        metadata=str({"openfood": True, "image": image_url})
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.post("/product", status_code=201)
def create_product(payload: ProductCreate, session = Depends(get_session)):
    statement = select(Product).where(Product.barcode == payload.barcode)
    existing = session.exec(statement).first()
    if existing:
        for k, v in payload.model_dump().items():
            setattr(existing, k, v)
        session.add(existing)
        session.commit()
        session.refresh(existing)
        return existing
    product = Product(**payload.dict())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product
