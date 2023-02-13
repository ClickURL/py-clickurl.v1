# In this file implemented 2st task
# I'm not sure how must look "controller" in this app. Maybe controller will be to complex for this small task
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

# Import model that do encode and decode to base64
from models.BaseModel import BaseModel

# Create instance of submodules of my app
router = APIRouter()

# 2nd task
# Inside this endpoint use method from BaseModel for decode a URL
# Use RedirectRespocse to redirect to target website
@router.get("/go/{url}", tags=["go"])
async def go(url: str):
    coder = BaseModel()
    result = coder.decode_url(url)
    return RedirectResponse(result)