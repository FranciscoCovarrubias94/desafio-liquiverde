from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    barcode: str
    name: str
    brand: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    weight_kg: Optional[float] = None
    packaging: Optional[str] = None
    estimated_carbon: Optional[float] = None