from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    email: EmailStr
    name: str
    password: str

    class Collection:
        name="users"

    class Config:
        schema_extra = {
            "example": {
              "email": "example@user.com",
              "name": "example python",
              "password": "password@123"
            }
        }

class TokenResponse(BaseModel): 
    access_token: str
    token_type: str