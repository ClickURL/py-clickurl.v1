from fastapi import Depends, APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from crud import user_crud
from schemas import user_schemas
from db.database import get_db

router = APIRouter(tags=["users"])

tempates = Jinja2Templates(directory='../frontend/public')

@router.get("/todo-users")
async def main(request: Request):
    return tempates.TemplateResponse('todo-users.html', {"request": request})

@router.get("/todo-users/user", response_model=list[user_schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/todo-users/user/{user_id}", response_model=user_schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User nor found")
    return user

@router.post("/todo-users/user", response_model=user_schemas.User)
def post_user(user_in: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user_in=user_in)