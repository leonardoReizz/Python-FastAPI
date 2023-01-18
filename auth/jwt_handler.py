import time
from datetime import datetimer
from database.connection import Settings
from fastapi import HTTPException, status
from jose import jwt, JWTError


def create_access_token(user: str):
  payload = {
    "user": user,
    "expire": time.time()+4000
  }
  token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
  return token

def verify_access_token(token: str):
  try: 
    data = jwt.encode(token, settings.SECRET_KEY, algorithm="HS256")
    expire = data.get("expire")

    if expire is None:
      raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Token expired"
      )
    return token
  
  except JWTError:
    raise  HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Invalid token"
    )