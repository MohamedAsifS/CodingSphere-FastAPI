from ..database import database
from sqlalchemy import Column,String,Integer


class Project(database.Base):
    __tablename__='projects'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    description=Column(String,nullable=True)