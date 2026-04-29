from pydantic import BaseModel

class UnityOfMeasureBase(BaseModel):
    name : str
    active : bool

class UnityOfMeasureCreate(UnityOfMeasureBase):
    pass

class UnityOfMeasure(UnityOfMeasureBase):
    id: int
    
    class Config:
        from_attributes = True