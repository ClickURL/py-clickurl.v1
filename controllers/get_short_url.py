# In this file implemented 3st task

# Import Form to be able get data from httpresponse from html page
from fastapi import Form, Request, APIRouter

# Jinja template engine for working with http methods on page
from fastapi.templating import Jinja2Templates

# Import model that do encode and decode to base64
from models.BaseModel import BaseModel

# Create instance of submodules of my app
router = APIRouter()

# Create a templates object that and use it later. Set the path of my html page
templates = Jinja2Templates(directory="pyblic")

# In httpget method create render of page and return page to client
# On this page user input his url address to be encoded
@router.get("/get_short_url", tags=["get_short_url"])
async def read_url(request: Request):
    get_url = ''
    return templates.TemplateResponse("get_short_url.html", {"request": request, "get_url": get_url})

# In httppost method server receive data from client, encodes URL with using BaseModel, 
# create render of page and return page to client with encoded URL like refferences
# to go "controller" from 2nd task
@router.post("/get_short_url", tags=["get_short_url"])
async def convert_url(request: Request, get_url = Form(...)):
    coder = BaseModel()
    get_url = coder.encode_url(get_url)
    add_path = request.url_for("go", url = get_url)
    return templates.TemplateResponse("get_short_url.html", {"request": request, "put_url": add_path})