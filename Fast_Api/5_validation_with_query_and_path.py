from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()

class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"
    
    
class Item(BaseModel):
    name: str
    price: float
    count: int
    id_: int 
    category: Category
    

items = {
    0: Item(name="Hammer", price=9.99, count=20, id_=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id_=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id_=2, category=Category.CONSUMABLES),
}


@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    
    return {"items": items}



@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist")
        
    return items[item_id]



Selection = dict[str, str | int | float | None | Category]


@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    
    def check_item(item: Item) -> bool:
        """ Check if the item matches the query arguments out of the scope """
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )
        
    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection
    }
    
    
    
@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id_ in items:
        HTTPException(status_code=400, detail="This item already exists")
    
    items[item.id_] = item 
    return {"added": item}


# We can place further restrictions on allowed arguments by using the Query and Path classes
# In this case we are setting a lower bound for valid values and a minimal length for the name 

@app.put("/update/{item_id}")
def update(
    item_id: int = Path(ge=0),
    name: str | None = Query(default=None, min_length=1, max_length=8),
    price: float | None = Query(default=None, gt=0.0),
    count: int | None = Query(default=None, ge=0),
) -> dict[str, Item]:
    
    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist")
        
    if all(value is None for value in (name, price, count)):
        HTTPException(status_code=400, detail="There are no parameters for update")
        
    item = items[item_id]
    if name is not None:
        item.name = name 
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count
    
    return {"updated": item}



@app.delete("/items/{item_id}")
def delete_item(item_id) -> dict[str, Item]:
    
    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist")
    
    item = items.pop(item_id)
    
    return {"deleted": item}

