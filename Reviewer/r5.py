from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.put("/users/update_name")
async def update_name(user_id: int, new_name: str):
 db[user_id] = new_name
 return {"status": "updated"}