def weighted_value(product: dict, weights: dict):
    price = product.get('price') or 0.0
    carbon = product.get('estimated_carbon') or 0.0
    utility = product.get('utility') or 1.0
    carbon_score = 1.0 / (1.0 + carbon)  
    utility_score = min(max(utility / 10.0, 0), 1)
    combined = weights.get('w_utility', 0.5) * utility_score + weights.get('w_carbon', 0.5) * carbon_score
    return combined

def knapsack_by_budget(products: list, budget: float, weights: dict = None, max_items: int = None):
    if weights is None:
        weights = {'w_utility':0.5, 'w_carbon':0.5}
    candidates = [p for p in products if (p.get('price') or 0) > 0]
    for p in candidates:
        p['_ratio'] = weighted_value(p, weights) / (p['price'] + 1e-9)
    candidates.sort(key=lambda x: x['_ratio'], reverse=True)
    chosen = []
    remaining = budget
    for p in candidates:
        if max_items and len(chosen) >= max_items:
            break
        if p['price'] <= remaining:
            chosen.append(p)
            remaining -= p['price']
    return chosen
