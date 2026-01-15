from fastapi import FastAPI
from models.model import Product
from models.database import session,Base,engine
from schemas.product import ProductCreate
import json

app=FastAPI(title="Inventory and Reorder API")

Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    with open('raw_data.json','r') as f:
        products=json.load(f)
    db=session()
    for item in products:
        product_data= ProductCreate(**item)
        db.add(Product(**product_data.model_dump())) 

    # db.commit()

# init_db()
        

@app.get("/products")
def get_products():
    return init_db()

@app.get("/")
def root():
    return{"message":"inventory api is running"}

@app.get("/health")
def health_check():
    return{"status":"ok"}


# @app.post("/products")
# def create_products(product: Product):


