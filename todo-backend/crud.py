from sqlalchemy.orm import Session

import models
import schemas


def get_todos(db: Session):
    return db.query(models.Todo).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)  # refresh to get the auto-generated id
    return db_todo


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def mark_completed(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db_todo.completed = True
        db.commit()
        db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
