from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool
    
    
@app.get('/')
def index():
    return {"message": "Hello, world!"}


@app.get('/greet/{name}')
def greet_name(name:str):
    return {"greeting":f"Hello {name}"}


@app.put('/item/{item_id}')
def update_item(item_id:int,item:Item):
    return {"name":item.name,
            "description":item.description,
            "price":item.price,
            "on_offer":item.on_offer,
            }