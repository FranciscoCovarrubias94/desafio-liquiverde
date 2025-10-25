# list_products.py
from sqlmodel import Session, select
from app.db import engine
from app.models import Product

def get_products(limit: int = 10):
    """Obtiene los primeros `limit` productos de la base de datos"""
    with Session(engine) as session:
        statement = select(Product).limit(limit)
        results = session.exec(statement).all()
        return results

if __name__ == "__main__":
    products = get_products()
    print("Lista de productos (limit 10):")
    for p in products:
        print(f"{p.barcode} | {p.name} | {p.brand} | {p.category} | ${p.price}")
