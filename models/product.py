from beanie import Document

class Product(Document):
  name: str
  price: float
  description: str

  class Settings:
    name= "products"

  class Config:
    schema_extra = {
      "example": {
        "name": "Table",
        "price": 99.9,
        "description": "This is a table"
      }
    }

