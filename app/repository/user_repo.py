from fastapi import HTTPException,status ,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schema import  user_schema
from ..models import user_model
from ..auth import hash,jwt_token


def register(request:user_schema.UserBase,db:Session):
    users=db.query(user_model.User).filter(user_model.User.username==request.username).first()
    if not users:
        if request.role not in ['admin','user']:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Role must be either admin or user")
        hashed=hash.Hash.hash(request.password)
        new_user=user_model.User(username=request.username,password=hashed,role=request.role)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return f"{new_user.username} created successfully"
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already exists")


def login(request:OAuth2PasswordRequestForm,db:Session):
    user=db.query(user_model.User).filter(user_model.User.username==request.username).first()
    if user:
        if hash.Hash.verify(request.password,user.password):
            print()
            access_token=jwt_token.get_access_token(data={'sub':user.username,'role':user.role})
            return {"access_token":access_token,"token_type":"bearer"}
        
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")