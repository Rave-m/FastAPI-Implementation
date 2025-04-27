from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Items(BaseModel):
    text: str 
    is_done: bool = False

items = []

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post('/items')
def create_item(items: Items):
    items.append(items)
    return items

@app.get('/items', response_model=list[Items])
def get_items(limit: int = 10):
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items[0:limit]

@app.get('/items/{item_id}', response_model=Items)
def get_item(item_id: int) -> Items:
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

