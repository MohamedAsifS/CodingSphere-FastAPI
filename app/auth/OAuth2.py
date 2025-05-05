from jose import jwt 
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from .jwt_token import verify

# it will help us to extract the token from the request header and then we can use this token to decode and get the user data
extract=OAuth2PasswordBearer(tokenUrl="user/login")
def get_current_user(token:str=Depends(extract)):
    print(token)
    creditionals_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    return verify(token,creditionals_exception)

