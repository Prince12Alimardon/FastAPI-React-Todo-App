from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Todo model
class Todo(BaseModel):
    title: str
    description: str = None
    completed: bool = False


# In-memory database
todos_db = []


# CRUD operations
@app.post("/todos/")
async def create_todo(todo: Todo):
    todos_db.append(todo)
    return todo


@app.get("/todos/", response_model=List[Todo])
async def read_todos():
    return todos_db


@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int):
    return todos_db[todo_id]


@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    todos_db[todo_id] = todo
    return {"message": "Todo has been updated successfully!"}


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    todos_db.pop(todo_id)
    return {"message": "Todo has been deleted successfully!"}
