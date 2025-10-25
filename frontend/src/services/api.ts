const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

export async function getProduct(barcode: string) {
  const res = await fetch(`${API_BASE}/product/${barcode}`);
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

export async function createProduct(payload: any) {
  const res = await fetch(`${API_BASE}/product`, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  return res.json();
}

export async function scoreProduct(barcodeOrProduct: any) {
  // Accepts {barcode:"..."} or {product: {...}}
  const res = await fetch(`${API_BASE}/score`, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(typeof barcodeOrProduct === 'string' ? {barcode: barcodeOrProduct} : {product: barcodeOrProduct})
  });
  return res.json();
}

export async function optimizeList(payload: any) {
  const res = await fetch(`${API_BASE}/optimize`, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  return res.json();
}

export async function findSubstitutes(barcode: string) {
  const res = await fetch(`${API_BASE}/substitute`, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({barcode})
  });
  return res.json();
}
