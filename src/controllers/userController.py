
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from src.dto.userDto import *
from fastapi.responses import RedirectResponse


# ------>

user_router = APIRouter(prefix='/user', tags=['User'])
template = Jinja2Templates(directory='src/views')


# ------>

@user_router.get('/login')
def login(
    request: Request
):
    """
    get page login.
    """
    return template.TemplateResponse(name='login.html', request=request)

@user_router.post('/login', include_in_schema=False)
def handleLogin(
    request: Request, 
    user_login_form: UserLoginFormDto = Form()
):
    """
    redirect from form login.
    """

    # TODO: build the context with user.

    return RedirectResponse(url='/index', status_code=303)


# ------>

@user_router.get('/createAcount')
def createUser(
    request: Request
):
    """
    get page login.
    """
    return template.TemplateResponse(name='createUser.html', request=request)

@user_router.post('/createAcount', include_in_schema=False)
def handleCreateUser(
    request: Request, 
    user_login_form: UserCreateFormDto = Form()
):
    """
    redirect from form login.
    """

    # TODO: build the context with user.

    return RedirectResponse(url='/index', status_code=303)