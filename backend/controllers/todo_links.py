from fastapi import Depends, APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from crud import url_crud
from schemas import url_schemas
from db.database import get_db

router = APIRouter(tags=["links"])

tempates = Jinja2Templates(directory='./frontend/public')

@router.get("/todo-links")
async def main(request: Request):
    return tempates.TemplateResponse('todo-links.html', {"request": request})
        
        
@router.get("/todo-links/link", response_model=list[url_schemas.UrlGet])
def get_urls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    links = url_crud.get_urls(db, skip = skip, limit = limit)
    return links


@router.get("/todo-links/link/{url_id}", response_model = url_schemas.UrlGet)
def get_url(url_id: int, db: Session = Depends(get_db)):
    link = url_crud.get_url(db, url_id = url_id)
    if not link:
        raise HTTPException(status_code=404, detail="URL not found")
    if link.deleted_by:
        raise HTTPException(status_code=404, detail="URL has been removed")
    return link


@router.post("/todo-links/link", response_model=url_schemas.UrlGet) #UrlCreate
def post_url(user_id: int, url_in: url_schemas.UrlCreate, db: Session = Depends(get_db)):
    return url_crud.create_url(db, url_in = url_in, user_id = user_id)



@router.delete("/todo-links/link/{url_id}", response_model=url_schemas.Url)
def delete_url(url_id: int, user_id: int, db: Session = Depends(get_db)):   
    link = url_crud.get_url(db, url_id = url_id)
    if not link:
        raise HTTPException(status_code=404, detail="URL not found")
    if link.created_by != user_id:
        raise HTTPException(status_code=403, detail="Forbiden, User not authorize")
    return url_crud.delete_url(db, url_id = url_id, user_id = user_id)