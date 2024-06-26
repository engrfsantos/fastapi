from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import sql_app
from sql_app import database
from sql_app import crud
from sql_app.crud import  models, schemas
from sql_app.database import engine, Base

app = FastAPI()

def create_db_and_tables():
    #sql_app.database.Base.metadata.create_all(bind=engine)    
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("Criou as tabelas")
    create_db_and_tables()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        print("Criou a sessão")
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=sql_app.schemas.User)
def create_user(user: sql_app.schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[sql_app.schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=sql_app.schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=sql_app.schemas.Item)
def create_item_for_user(
    user_id: int, item: sql_app.schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[sql_app.schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items