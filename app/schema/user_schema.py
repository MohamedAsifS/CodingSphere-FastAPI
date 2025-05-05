from pydantic import BaseModel 


class UserBase(BaseModel):
    username:str 
    password:str 
    role:str
class Login(BaseModel):
    username:str
    password:str