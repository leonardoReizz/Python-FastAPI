from database.connection import Database
from fastapi import APIRouter
from models.product import Product
product_router = APIRouter(tags=["product"])
product_database = Database(Product)

@product_router.post('/')
async def create_product(product: Product):
  product = await product_database.save(product)
  print("a")
  print(product)
  return {
    "message": product 
  }

@product_router.delete('/{productId}')
async def delete_product(productId: str):
  deleteProduct = await product_database.delete(productId)

  if deleteProduct:
    return {
      "message" : "Product deleted"
    }
  
  return {
    "message": "Product not deleted"
  }
    
@product_router.get('/')
async def list_products():
  list = await product_database.get_all()

  return { "message" : list }

@product_router.get('/{productId}')
async def find_product_by_id(productId: str):
  find = await product_database.get(productId)

  return { "message" : find }

@product_router.put('/{productId}')
async def update_product(productId: str, product: Product):
  update = await product_database.update(productId, product)

  return { "message" : update }
