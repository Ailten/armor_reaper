
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates

from src.dto.userDto import *
from src.models.user import User
from fastapi.responses import RedirectResponse

from src.services.userService import UserService
from src.models.database import get_db_session

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlalchemy.orm import Session


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
    user_login_form: UserCreateFormDto = Form(),
    session: Session = Depends(get_db_session)
):
    """
    redirect from form login.
    """

    user_service = UserService(session)

    e_mail = user_login_form.e_mail.lower()
    user = user_service.getByEMail(e_mail)

    if user != None:
        # TODO: inclue an error message : 'this e_mail already has an acount'.
        return RedirectResponse(url='/createAcount', status_code=303)
    
    # TODO: hash.
    password_hash = user_login_form.password

    user = User(
        e_mail=e_mail,
        password=password_hash,
        pseudo=user_login_form.pseudo
    )
    
    try:
        user_service.create(user)
    except Exception as e:
        session.rollback()
        # TODO: sent error message : 'an error raise from the database'.
        return RedirectResponse(url='/createAcount', status_code=303)

    user_session = UserSessionDto(
        id=user.id,
        e_mail=user.e_mail,
        pseudo=user.pseudo
    )
    request.session["user"] = user_session

    return RedirectResponse(url='/index', status_code=303)