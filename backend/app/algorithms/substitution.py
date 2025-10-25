from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_substitutes(target: dict, candidates: List[dict], top_k=5):
    """
    target: product dict
    candidates: list of product dicts
    strategy:
      - filter by same category
      - compute textual similarity on name/ingredients (TF-IDF)
      - sort by (similarity desc, sustainability score asc)
    """
    
    filtered = [c for c in candidates if c.get('category') == target.get('category') and c.get('barcode') != target.get('barcode')]
    if not filtered:
        filtered = [c for c in candidates if c.get('barcode') != target.get('barcode')]

    texts = [target.get('name','')] + [c.get('name','') for c in filtered]
    vec = TfidfVectorizer().fit_transform(texts)
    sims = cosine_similarity(vec[0:1], vec[1:]).flatten()
    scored = []
    for c, sim in zip(filtered, sims):
        sustainability_score = (c.get('estimated_carbon') or 0) 
        scored.append((c, sim, sustainability_score))
    scored.sort(key=lambda x: (-x[1], x[2]))
    return [s[0] for s in scored[:top_k]]
