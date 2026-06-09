from fake_db import database
from exceptions.exceptions import DuplicateTodoError
from fastapi import HTTPException

async def get_all():
    return await database.get_all()

async def get_by_title(title:str):
    try:
        for i in database.data:
            if i['title'].lower().strip() == title.lower().strip():
                return i
    except Exception as e:
        return e

async def add_todo(new_todo:dict):
    try:
        await database.add_todo(new_todo)
        return new_todo
    except DuplicateTodoError:
        raise HTTPException(status_code=409)
    
async def remove_todo(todo_id:int):
    return await database.delete_todo(todo_id)

async def update_todo(todo_id:int, todo:dict):
    return await database.update_todo(todo_id, todo)