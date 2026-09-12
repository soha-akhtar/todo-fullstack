from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud
import models
import schemas
from database import Base, SessionLocal, engine

# Create the database tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency that provides a database session to each request
# and always closes it afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo."""
    return crud.create_todo(db, todo)


@app.get("/todos", response_model=list[schemas.TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    """Return every todo in the database."""
    return crud.get_todos(db)


@app.put("/todos/{todo_id}/complete", response_model=schemas.TodoResponse)
def complete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Mark a specific todo as completed."""
    db_todo = crud.mark_completed(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a specific todo."""
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": f"Todo {todo_id} deleted successfully"}
