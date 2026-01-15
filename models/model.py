from pydantic import BaseModel,Field

class Product(BaseModel):
    name: str 
    current_stock: int = Field(... , ge=0)
    min_reorder_level: int = Field(... , ge=1)
    price: float