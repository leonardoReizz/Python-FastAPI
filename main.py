from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
  name: str
  price: float
  aaaa: float

app = FastAPI()


@app.get('/')
def read_root():
  message = "Hello World"
  return {  "message":  message } 

@app.get('/items/{itemId}')
def get_item_by_id(itemId: int, q: Union[str, None] = None):
  return { "itemId": itemId, "Nao sei o que e " : q}

@app.put('/item/{itemId}')
def update_item(itemId: int, item: Item):
  return { "itemId": itemId, "item": item }

@app.post('/item')
def create_item(item: Item):
    return { "item": item }


@app.post('/compras')
def create_item(item: Item):
    return { "item": item }

