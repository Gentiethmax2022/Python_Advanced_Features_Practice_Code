from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    TOOLS = "tools"
    CUNSUMABLES = "consumables"
    
    
class Item(BaseModel):
    name: str
    price: float
    count: int
    id_: int
    category: Category
    
    
items = {
    0: Item(name="Hammer", price=45.89, count=20, id_=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=89.90, count=23, id_=1, category=Category.TOOLS),
    3: Item(name="Nails", price=1.99, count=390, id_=3, category=Category.CUNSUMABLES)
}

# FastAPI handles json serialization and deserialization for us 
# We can simply use built-in python and Pydantic types, in this case dict[int, Item]

@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


