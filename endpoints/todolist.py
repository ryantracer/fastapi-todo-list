from fastapi import APIRouter
from services import todos
from models.todo import TodoBase, TodoResponse

router = APIRouter(
    prefix='/todos',
    tags=['todos'],
    responses={404:{'description':'Not found'}},
)

@router.get('/')
async def get_todos() -> list[TodoResponse]:
    return await todos.get_all()

@router.get('/{todo_title}')
async def get_todo_by_title(todo_title:str) -> TodoResponse:
    return await todos.get_by_title(todo_title)

@router.post('/')
async def add_todo(todo:TodoBase) -> TodoResponse:
    return await todos.add_todo(todo.model_dump())

@router.delete('/{todo_id}')
async def delete_todo(todo_id:int):
    return await todos.remove_todo(todo_id)

@router.put('/{todo_id}')
async def update_todo(todo_id:int, todo:TodoBase) -> TodoResponse:
    return await todos.update_todo(todo_id, todo)