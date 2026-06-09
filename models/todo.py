from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title:str
    description:Optional[str] = None
    done:bool = False

class TodoResponse(TodoBase):
    id:int