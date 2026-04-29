from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name : str = Field(..., min_length = 1, max_length = 100)
    price : float = Field(..., gt = 0)
    description : str | None = Field(None, max_length = 500)
    image_url : str | None = Field(None, max_length = 200)
    
    category_id : int
    unity_of_measure_id : int
    status_id : int

class ProductCreate(ProductBase):
    pass
    
class Product(ProductBase):
    id : int

    class Config:
        from_attributes = True

