from typing import Optional
from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    barcode: str
    name: str
    brand: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    weight_kg: Optional[float] = None
    packaging: Optional[str] = None
    estimated_carbon: Optional[float] = None