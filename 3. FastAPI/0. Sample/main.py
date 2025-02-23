from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str
    is_done: bool = False
    

items = []

@app.get('/')
def root():
    return {'Hello': 'World'}

@app.get('/items')
def limit_items(limit: int = 10):
    return items[0:limit]

@app.post('/items', response_model=list[Item])
def create_item(item: Item) -> list[Item]:
    items.append(item)
    return items

@app.get('/items/{item_id}')
def get_item(item_id: int):
    if (item_id > len(items)):
        raise HTTPException(status_code=404, detail='Item not found')
    item = items[item_id]
    return item
