from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from database import SessionLocal

app=FastAPI()

class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode=True


db=SessionLocal()

    
@app.get('/items')
def get_all_items():
    pass

@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass

@app.post('/items')
def create_an_item():
    pass

@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    pass