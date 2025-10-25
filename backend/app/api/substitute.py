from fastapi import APIRouter, Body, Depends, HTTPException
from app.db import get_session
from app.models import Product
from sqlmodel import select
import difflib

router = APIRouter()

def simple_name_similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a or "", b or "").ratio()

@router.post("/substitute")
def substitute(payload: dict = Body(...), session = Depends(get_session)):
    barcode = payload.get('barcode')
    top_k = payload.get('top_k', 5)
    target = session.exec(select(Product).where(Product.barcode == barcode)).first()
    if not target:
        raise HTTPException(status_code=404, detail="Not Found")
    candidates = session.exec(select(Product)).all()
    # filter same category first
    same_cat = [c for c in candidates if c.category == target.category and c.barcode != barcode]
    pool = same_cat if same_cat else [c for c in candidates if c.barcode != barcode]
    scored = []
    for c in pool:
        sim = simple_name_similarity(target.name, c.name)
        # favor lower carbon
        carbon = c.estimated_carbon or 9999
        scored.append((c, sim, carbon))
    scored.sort(key=lambda x: (-x[1], x[2]))
    subs = [s[0].dict() for s in scored[:top_k]]
    return {'substitutes': subs}
