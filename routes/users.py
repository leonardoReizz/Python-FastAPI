from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.connection import Database
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User, UserSignIn, TokenResponse

user_router = APIRouter(tags=["user"])
user_database = Database(User)
hash_password = HashPassword()

@user_router.post('/signup')
async def create_user(user: User) -> dict:
  user_exist = await User.find_one(User.email == user.email)
  if user_exist:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="User with email provided exist already"
    )
  hashed_password = hash_password.create_hash(user.password)
  user.password = hashed_password
  await user_database.save(user)
  return {
    "message": "User created successfuly"
  }

@user_router.post('/signin', response_model = TokenResponse)
async def sign_user_in(user: UserSignIn) -> dict:
  user_exist = await User.find_one(User.email == user.email)

  if not user_exist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User with email does not exist"
    )
  
  if hash_password.verify_hash(user.password, user_exist.password):
    access_token = create_access_token(user_exist.email)

    return {
      "access_token" : access_token,
      "token_type": "Bearer"
    }
  
  raise HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid details passed"
  )