from fastapi import APIRouter, Body, HTTPException
from app.algorithms.multiobjective_knapsack import knapsack_by_budget

router = APIRouter()

@router.post("/optimize")
def optimize_list(payload: dict = Body(...)):
    """
    Espera:
    {
      "products": [ {producto1}, {producto2}, ... ],
      "budget": 10.0,
      "weights": {"w_utility": 0.5, "w_carbon": 0.5},
      "max_items": 5
    }
    """
    products = payload.get("products")
    budget = payload.get("budget")
    if not products or budget is None:
        raise HTTPException(status_code=400, detail="products and budget required")
    
    weights = payload.get("weights") or {"w_utility":0.5, "w_carbon":0.5}
    max_items = payload.get("max_items")
    optimized = knapsack_by_budget(products, budget, weights, max_items)
    return {"optimized": optimized}
