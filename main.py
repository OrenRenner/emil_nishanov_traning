import pandas as pd
from model.lr import fc, add
import json
from fastapi import FastAPI, Body
from pydantic import BaseModel
from io import StringIO
from typing import Union
import worker


app = FastAPI(
    title="Optimization API 2",
    description="API for optimization",
    version="2.0.1",
)

class ItemSchemaA(BaseModel):
    opti_type: str
    scenario_id: str

class ItemSchemaB(BaseModel):
    env: str
    lang: str

class Item(BaseModel):
    item: Union[ItemSchemaA, ItemSchemaB]


class ItemAdd(BaseModel):
    a: int
    b: int


@app.post("/optimize")
async def optimize(item: ItemSchemaA | ItemSchemaB):
    # Ваша логика обработки запроса

    return {"Hello": item, "type": isinstance(item, ItemSchemaA)}


@app.post("/")
async def read_root(data = Body(..., media_type="text/csv")):
    df = pd.read_csv(StringIO(data.decode(encoding='utf8')))
    y = fc(df)
    return {"Hello": str(y)}


@app.post("/add")
async def read_root(data: ItemAdd):
    task = worker.create_task.delay(data.a, data.b)
    return {"task_id": str(task.id)}


@app.get("/add/{task_id}")
async def read_root(task_id: str):
    task = worker.create_task.AsyncResult(task_id)
    return {"task_id": str(task.state), "result": task.result}
