from fastapi import FastAPI,Depends,HTTPException
from models.model import Product
from models.database import session,Base,engine
from schemas.product import ProductCreate
from sqlalchemy.orm import Session
import json

app=FastAPI(title="Inventory and Reorder API")

Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# def init_db():
#     with open('raw_data.json','r') as f:
#         products=json.load(f)
#     db=session()
#     for item in products:
#         product_data= ProductCreate(**item)
#         db.add(Product(**product_data.model_dump())) 

#     db.commit()

# init_db()
        
@app.get("/products")
def get_products(db : Session = Depends(get_db)):
    db_products = db.query(Product).all()
    return db_products

@app.post("/products")
def create_product( product : ProductCreate , db : Session = Depends(get_db) ):
    db.add(Product(**product.model_dump()))
    db.commit()
    return {"message": "Product created successfully"}


@app.put("/products/{product_id}")
def update_product(product_id : int , product: ProductCreate, db : Session = Depends(get_db)):
    db_product=db.query(Product).filter(Product.id==product_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="product not found")
    
    db_product.name=product.name
    db_product.current_stock = product.current_stock
    db_product.min_reorder_level = product.min_reorder_level
    db_product.price = product.price

    db.commit()
    return {"message": "Product updated successfully"}


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()

    return {"message": "Product deleted successfully"}

@app.get("/inventory/reorder_recommendations")
def reorder_recommendation(db: Session = Depends(get_db)):

    products=db.query(Product).all()
    reorder_list=[]
    for p in products:
        if p.current_stock <= p.min_reorder_level*1.25:
            reorder_list.append(p)
    return reorder_list


# @app.post("/products")
# def check():
#     return{"message":"inventory api is running"}


@app.get("/")
def health_check():
    return{"status":"ok"}


