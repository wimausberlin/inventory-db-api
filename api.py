from http.client import HTTPException
from fastapi import FastAPI
from numpy import delete
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    title: str
    detail: str

todo_db=[]

@app.get("/sum/{a}/{b}")
async def root(a:int,b:int):
    return {"sum": a+b,
            "diff":a-b}

@app.post("/todo/add")
async def create_todo(todo:Todo):
    todo_db.append(todo)
    return todo

@app.get("/todo/get/{id}")
async def get_todo(id:int):
    try:
        return todo_db[id]
    except:
        raise HTTPException(status_code=404,detail="Todo not found")

@app.put("/todo/update/{id}")
async def update_todo(id:int,todo:Todo):
    try:
        todo_db[id]=todo
        return todo_db[id]
    except:
        raise HTTPException(status_code=404,detail="Todo not found")

@app.delete("/todo/delete/{id}")
async def delete_todo(id:int):
    try:
        todo_db.pop(id)
    except:
        raise HTTPException(status_code=404,detail="Todo not found")