from fastapi import FastAPI
from models.model import Product
from models.database import session,Base,engine
from schemas.product import ProductCreate

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Inventory and Reorder API")

@app.get("/")
def root():
    return{"message":"inventory api is running"}

@app.get("/health")
def health_check():
    return{"status":"ok"}


# @app.post("/products")
# def create_products(product: Product):


