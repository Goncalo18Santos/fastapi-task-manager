from app.schemas import TaskCreate, TaskUpdate, TaskInDB
from sqlalchemy import select, update, delete
from fastapi import FastAPI, HTTPException
from app.db import database
from app.models import tasks
from fastapi.responses import JSONResponse

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"message": "Hello from Task Manager API with DB!"}

@app.get("/tasks")
async def get_tasks():
    query = tasks.select()
    results = await database.fetch_all(query)
    return JSONResponse(results)

@app.post("/tasks/", response_model=TaskInDB)
async def create_task(task: TaskCreate):
    query = tasks.insert().values(title=task.title)
    task_id = await database.execute(query)
    return {**task.dict(), "id": task_id}

@app.get("/tasks/{task_id}", response_model=TaskInDB)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=TaskInDB)
async def update_task(task_id: int, task: TaskUpdate):
    query = tasks.update().where(tasks.c.id == task_id).values(title=task.title)
    await database.execute(query)
    return {**task.dict(), "id": task_id}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {"detail": "Task deleted"}
