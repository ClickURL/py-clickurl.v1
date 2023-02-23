from sqlalchemy.orm import Session, joinedload

from schemas.url_schemas import UrlCreate
from models.url_model import Url

def get_url(db: Session, url_id: int):
    return db.query(Url).where(Url.id == url_id).one()

def get_urls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Url).where(Url.deleted_by == None).offset(skip).limit(limit).all()

def create_url(db: Session, url_in: UrlCreate, user_id: int):
    db_url = Url(
        value = url_in.value,
        created_at = url_in.created_at,
        created_by = user_id
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def delete_url(db: Session, url_id: int, user_id: int):
    db_url = db.query(Url).filter(Url.id == url_id).first()
    db_url.deleted_by = user_id
    db.commit()
    return db_url