from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/data/{item_id}")
async def get_data(item_id: int = Query(...)):
 return {"status":"updated"}