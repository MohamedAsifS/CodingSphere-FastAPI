from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from ..schema import  user_schema
from ..database import database
from ..repository import user_repo
from fastapi.security import OAuth2PasswordRequestForm



router=APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/register",status_code=status.HTTP_201_CREATED)
def register(request:user_schema.UserBase,db:Session=Depends(database.get_db)):
    return user_repo.register(request,db)


@router.post("/login",status_code=status.HTTP_200_OK)
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    return user_repo.login(request,db)