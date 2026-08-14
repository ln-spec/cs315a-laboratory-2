from fastapi import FastAPI, Path, Query
from typing import Optional


app = FastAPI()

@app.get("/inventory/{item_id}")
async def get_inventory_item(
item_id: int = Query(..., min_length=1),
category: str = Path(..., max_length=15),
discount: float = Query(0.0, gt=100.0)):
 return {"item_id": item_id, "category": category, "discount": discount}













  
