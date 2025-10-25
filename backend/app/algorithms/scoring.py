def compute_product_score(product: dict, weights: dict = None) -> dict:
    # weights defaults
    if weights is None:
        weights = {'econ':0.4, 'env':0.4, 'soc':0.2}
    price = product.get('price')
    carbon = product.get('estimated_carbon')
    # economic: cheaper = better. Heuristic: if no price -> neutral 50
    if price is None:
        econ = 50.0
    else:
        # assume price realistically between 0 and 50; clamp and invert
        econ = max(0.0, min(100.0, (1 - (price / 50.0)) * 100))
    # environmental: lower carbon better; if absent -> neutral
    if carbon is None:
        env = 50.0
    else:
        env = max(0.0, min(100.0, (1 - (carbon / 10.0)) * 100))
    # social: heuristic from packaging/metadata
    soc = 50.0
    pack = product.get('packaging', '') or ''
    if 'recycl' in pack.lower():
        soc += 20
    soc = min(100, soc)
    overall = econ * weights['econ'] + env * weights['env'] + soc * weights['soc']
    return {'econ': round(econ,2), 'env': round(env,2), 'soc': round(soc,2), 'overall': round(overall,2)}
