from pydantic import BaseModel

class ProjectBase(BaseModel):
    
    name:str 
    description:str 
    
class ProjectShow(BaseModel):
        
        id:int 
        name:str 
        description:str 
        
        class Config:
            orm_mode = True