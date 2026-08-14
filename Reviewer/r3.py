from fastapi import FastAPI, Path, Query
from typing import Optional


app = FastAPI()

@app.get("/search")
async def search(term: Optional[str] = Query(None, max_length=10, min_length=3)):
 return {"term": term}