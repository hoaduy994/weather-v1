from pydantic import BaseModel
    
class InfoSchema(BaseModel):
    id:int
    name:str
    ip:str
    time:str
    
    class Config:
        orm_model=True 