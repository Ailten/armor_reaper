
from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles
import src.controllers as controllers

from starlette.middleware.sessions import SessionMiddleware

from os import getenv
from dotenv import load_dotenv


# ------>

app = FastAPI()

load_dotenv()

# for make session navigation.
app.add_middleware(
    SessionMiddleware,
    secret_key=getenv('SESSION_SECRET_KEY')
)

app.mount('/public', StaticFiles(directory='src/public'), name='public')

# include all route controller.
for item_name in dir(controllers):
   item = getattr(controllers, item_name)
   if isinstance(item, APIRouter):
       app.include_router(item)

template = Jinja2Templates(directory="src/views")


# ------>

@app.get("/")
async def baseRoot(request: Request):
    """
    end point for index view.
    """
    return template.TemplateResponse(
        name='index.html', 
        request=request, 
        context={}
    )