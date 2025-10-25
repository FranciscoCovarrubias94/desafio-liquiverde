from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import init_db
from .api import products, scoring, optimize, substitute

app = FastAPI(title="LiquiVerde API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api/v1")
app.include_router(scoring.router, prefix="/api/v1")
app.include_router(optimize.router, prefix="/api/v1")
app.include_router(substitute.router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    init_db()