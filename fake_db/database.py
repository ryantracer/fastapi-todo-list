from json import load, dump
from pathlib import Path
from exceptions.exceptions import DuplicateTodoError
from fastapi import HTTPException


BASE_DIR = Path(__file__).parent


async def get_all():
    with open(BASE_DIR / 'source.json', 'r') as f:
        return load(f)
    
async def add_todo(item:dict):
    data = await get_all()
    found_equal = False
    
    if len(data) > 0:
        new_id = data[-1]['id'] + 1
    else:
         new_id = 1
    
    item['id'] = new_id
    
    for i in data:
         if i['title'].lower().strip() == item['title'].lower().strip():
            found_equal = True
            break
        
    if not found_equal:
        data.append(item)
        with open(BASE_DIR / 'source.json', 'w') as f:
            dump(data, f, indent=2)
        
    else:
        raise DuplicateTodoError()
    
async def delete_todo(todo_id:int):
    data = await get_all()
    new_list = [i for i in data if i['id'] != todo_id]
    if len(data) == len(new_list):
        return 'Not Found my dude'
    else:        
        with open(BASE_DIR / 'source.json', 'w') as f:
            dump(new_list, f, indent=2)
        return 'Destroyed :P'
    
async def update_todo(todo_id:int, todo:dict):
    data = await get_all()
    for index, item in enumerate(data):
        if item['id'] == todo_id:
            todo['id'] = todo_id
            data[index] = todo.model_dump()
            with open(BASE_DIR / 'source.json', 'w') as f:
                dump(data, f, indent=2)
            return data