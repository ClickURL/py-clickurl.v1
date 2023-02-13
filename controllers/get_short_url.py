# In this file implemented 3st task

# Import Form to be able get data from httpresponse from html page
from fastapi import Form, Request, APIRouter

# Jinja template engine for working with http methods on page
from fastapi.templating import Jinja2Templates

# Import model that do encode and decode to base64
from models.Converter import Converter

# Create instance of submodules of my app
router = APIRouter()

# Create a templates object that and use it later. Set the path of my html page
templates = Jinja2Templates(directory="public")


# In httpget method create render of page and return page to client
# On this page user input his url address to be encoded
@router.get("/get_short_url")
async def read_url(request: Request):
    return templates.TemplateResponse("get_short_url.html", {
        "request": request,
        "original_url": "",
        "result_short_url": "",
    })


# In httppost method server receive data from client, encodes URL with using BaseModel,
# create render of page and return page to client with encoded URL like refferences
# to go "controller" from 2nd task
@router.post("/get_short_url")
async def convert_url(request: Request, original_url=Form(...)):
    coder = Converter()

    result_short_url = request.url_for("go", url=coder.encode_url(original_url))
    return templates.TemplateResponse("get_short_url.html", {
        "request": request,
        "original_url": original_url,
        "result_short_url": result_short_url,
    })
