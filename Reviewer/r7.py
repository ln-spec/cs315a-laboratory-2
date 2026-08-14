from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/check/")
async def check(flag: bool = Query(False)):
 return {"flag": flag}
