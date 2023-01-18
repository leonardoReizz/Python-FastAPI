import uvicorn
from auth.authenticate import oauth2_scheme
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.product import product_router
from database.connection import Settings
from routes.users import user_router

app = FastAPI()

settings = Settings()

origins = [
    "*",
    "http://localhost",
    "https://localhost:3000",
    "https://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(user_router, prefix="/user")
app.include_router(product_router, prefix="/product", dependencies=[Depends(oauth2_scheme)])

@app.on_event("startup")
async def init_db():
  await settings.initialize_database()

@app.get("/")
async def home():
  return { "message" : "ok"}


if __name__ == '__main__':
  uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)