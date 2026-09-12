from typing import Optional

from pydantic import BaseModel


# Fields the client sends when creating a todo
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None


# Fields returned to the client in API responses
class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        # Allows Pydantic to read data directly from SQLAlchemy model objects
        orm_mode = True
