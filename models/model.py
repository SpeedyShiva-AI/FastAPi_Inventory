from sqlalchemy import Integer, Float, String, Column
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=False)
    name = Column(String)
    current_stock = Column(Integer)
    min_reorder_level = Column(Integer)
    price = Column(Float)
    
