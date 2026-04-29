from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name : str = Field(..., min_length=3, max_length=50, )
    active : bool = True
    
class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id : int

    class Config:
        from_attributes = True