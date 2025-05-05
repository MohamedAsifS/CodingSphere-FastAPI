from fastapi import HTTPException
from jose import jwt,ExpiredSignatureError
from datetime import timedelta, datetime
from typing import Optional
from environs import Env
from ..schema import token_schema

env=Env()
env.read_env()

# we have to set the secret key for jwt token and alogorthim we use to encode and access time for access token 
ACCESS_SECURITY_KEY=env("ACCESS_SECURITY_KEY")
ALGORITHIM=env("ALGORITHIM")
ACCESS_TIME_EXPIRE_MINUTE=30


def get_access_token(data:dict,expires_delta:Optional[timedelta]=None):
    """
    Generate a access token with a given expiry.
    """
    to_encode=data.copy()
    if expires_delta:
        expires=datetime.utcnow()+expires_delta
    else:
        expires=datetime.utcnow()+timedelta(ACCESS_TIME_EXPIRE_MINUTE)
    to_encode.update({'exp':expires})
    encode_jwt=jwt.encode(to_encode,ACCESS_SECURITY_KEY,algorithm=ALGORITHIM)
    return encode_jwt



def verify_token(token:str,credtional_exception:HTTPException):
    """Decode the token and check if the token is valid or not"""
    
    try:
        payload=jwt.decode(token,ACCESS_SECURITY_KEY,algorithms=[ALGORITHIM])
        if not payload['sub'] or not payload['role']:
            raise credtional_exception
        return token_schema.Token(username=payload['sub'],role=payload['role'])
    except ExpiredSignatureError:
        raise Exception("Token expired")
    except credtional_exception:
        raise credtional_exception