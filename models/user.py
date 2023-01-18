from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
	email: EmailStr
	username: str
	password: str

	class Settings:
		name = "users"

	class Config:
		schema_extra = {
			"example": {
				"email": "example@user.com",
				"username": "example python",
				"password": "password@123"
			}
		}


class UserSignIn(BaseModel):
	email: EmailStr
	password: str

	class Config: 
		schema_extra = {
			"example" : {
				"email": "user@xample.com",
				"password": "password@123"
			}
		}

class TokenResponse(BaseModel):
	access_token: str
	token_type: str
