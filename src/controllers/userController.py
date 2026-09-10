
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates

from src.dto.userDto import *
from src.models.user import User
from fastapi.responses import RedirectResponse

from src.services.userService import UserService
from src.models.database import get_db_session
from sqlalchemy.orm import Session

from src.utils.errorInjecor import injectError, resetError, redirectError, reachThePage

from src.utils.crypt import hashStr, compareHash
from src.utils.sanitise import htmlSanitise


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

    resetError(request.session)

    reachThePage(request.session)
    return template.TemplateResponse(name='login.html', request=request)

@user_router.post('/login', include_in_schema=False)
def handleLogin(
    request: Request, 
    user_login_form: UserLoginFormDto = Form(),
    session: Session = Depends(get_db_session)
):
    """
    redirect from form login.
    """

    resetError(request.session)

    user_service = UserService(session)

    e_mail = user_login_form.e_mail.lower()
    user = user_service.getByEMail(e_mail)

    # no user with this email.
    if user == None:
        
        injectError(request.session, 'e_mail or password invalid')

        redirectError(request.session)
        return RedirectResponse(url='/user/login', status_code=303)
    
    # compare hash password.
    if not compareHash(user_login_form.password, user.password):

        injectError(request.session, 'e_mail or password invalid')

        redirectError(request.session)
        return RedirectResponse(url='/user/login', status_code=303)

    # log.
    user_session = castUserAsSessionDto(user)
    request.session['user'] = user_session.model_dump()

    redirectError(request.session)
    return RedirectResponse(url='/', status_code=303)


# ------>

@user_router.get('/createAcount')
def createUser(
    request: Request
):
    """
    get page login.
    """

    resetError(request.session)

    reachThePage(request.session)
    return template.TemplateResponse(name='createUser.html', request=request)

@user_router.post('/createAcount', include_in_schema=False)
def handleCreateUser(
    request: Request, 
    user_create_form: UserCreateFormDto = Form(),
    session: Session = Depends(get_db_session)
):
    """
    redirect from form login.
    """

    resetError(request.session)

    user_service = UserService(session)

    e_mail = user_create_form.e_mail.lower()
    user = user_service.getByEMail(e_mail)

    if user != None:
        
        injectError(request.session, 'this e_mail already has an acount')

        redirectError(request.session)
        return RedirectResponse(url='/user/createAcount', status_code=303)
    
    # hash password.
    password_hash = hashStr(user_create_form.password)

    user = User(
        e_mail=e_mail,
        password=password_hash,
        pseudo=htmlSanitise(user_create_form.pseudo)
    )
    
    try:
        user_service.create(user)
    except Exception as e:
        session.rollback()
        
        injectError(request.session, 'an error raise from the database')
        
        redirectError(request.session)
        return RedirectResponse(url='/user/createAcount', status_code=303)

    # log.
    user_session = castUserAsSessionDto(user)
    request.session['user'] = user_session.model_dump()

    redirectError(request.session)
    return RedirectResponse(url='/', status_code=303)


# ------>

@user_router.get('/logout')
def logout(
    request: Request
):
    """
    logout user and redirect to index.
    """

    resetError(request.session)

    # remove user from session.
    if 'user' in request.session:
        del request.session['user']

    redirectError(request.session)
    return RedirectResponse(url='/', status_code=303)
