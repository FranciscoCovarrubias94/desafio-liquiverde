from fastapi import APIRouter, Body, Depends, HTTPException
from app.db import get_session
from app.models import Product
from app.algorithms.scoring import compute_product_score
from sqlmodel import select

router = APIRouter()

@router.post("/score")
def score(payload: dict = Body(...), session = Depends(get_session)):
    """
    payload can be: {"barcode":"12345"} or full product dict
    """
    if 'barcode' in payload:
        barcode = payload['barcode']
        p = session.exec(select(Product).where(Product.barcode == barcode)).first()
        if not p:
            raise HTTPException(status_code=404, detail="Not Found")
        product = p.dict()
    else:
        product = payload.get('product')
        if not product:
            raise HTTPException(status_code=400, detail="product field required")
    return compute_product_score(product)
