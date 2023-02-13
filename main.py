# Main file endpoint of my application
# In this file implemented 1st task
import uvicorn
from fastapi import FastAPI

# Import submodule for 2. task
from controllers import go

# Import submodule for 3. task
from controllers import get_short_url

# Import model that do encode and decode to base64
from models.BaseModel import BaseModel

# Create instance of my application
app = FastAPI()

# Now we add each our routers to main FastAPI applocation 
app.include_router(go.router)
app.include_router(get_short_url.router)

# Default page
@app.get("/")
async def root():
    return "Hell World"

# Page for 1. task
# Inside this endpoint use method from BaseModel for encode a URL
@app.post("/base64")
async def base64(url: str):
    coder = BaseModel()
    result = coder.encode_url(url)
    return {"result":result}

# Setting for run the application on the specified localhost and port (from hte Base64 issues)
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)