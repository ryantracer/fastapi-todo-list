from fastapi import FastAPI
from endpoints import todolist

app = FastAPI(title='Todo List')

app.include_router(todolist.router)
