from sqlalchemy.orm import Session

from schemas.user_schemas import UserCreate
from models.user_model import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user_in: UserCreate):
    db_user = User(
        name = user_in.name,
        created_at = user_in.created_at
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user