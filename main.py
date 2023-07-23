from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

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

    
@app.get('/items', response_model=List[Item])
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass

@app.post('/items',response_model=Item,
          status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db.add(new_item)

@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    pass