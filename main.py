from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float

items_db = {}
@app.get('/')
def read_root():
    return {"message":"Welcome to the API"}

@app.post('/items/{item_id}')
def create_item(item_id: int,item:Item):
    items_db[item_id] = item
    return {"message":f"Item with id{item_id} created successfully"}

@app.get('/item/{item_id}')
def read_item(item_id:int):
    item = items_db.get(item_id)
    if item:
        return item
    return {"message": f"Item with id {item_id} not found"}
