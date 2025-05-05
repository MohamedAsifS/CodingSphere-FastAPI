from sqlalchemy import Column, Integer,String 
from sqlalchemy.orm import relationship
from  app.database import database

class User(database.Base):
    __tablename__="users"
    username=Column(String,primary_key=True,index=True)
    password=Column(String,nullable=False)
    role=Column(String,nullable=False)