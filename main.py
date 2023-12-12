## FastAPI - Construção de API
## Uvicorn - Hospedagem da API local
# uvicorn main:app --reload

# Fast
# Documentação automática (/docs)
# Gerenciamento de processos assíncronos

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

itens = {} # Simulating a Database
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def home():
    return "HOME"

@app.get("/items/", response_model=itens)
async def read_items():
    return itens
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    itens[item.name] = item
    return item

@app.put("/items/")
async def update_item(item: Item):
    item_to_update = item
    if item.name in itens:
        itens[item.name] = item
        return item
    else:
        return {"Item not found."}
