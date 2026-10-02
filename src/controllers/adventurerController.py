

from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates

from src.dto.adventurerDto import *
from src.models.adventurer import Adventurer
from src.models.joinAdventurerTreeSkill import JoinAdventurerTreeSkill
from fastapi.responses import RedirectResponse

from src.services.userService import UserService
from src.services.adventurerService import AdventurerService
from src.services.joinAdventurerTreeSkillService import JoinAdventurerTreeSkillService
from src.services.treeSkillService import TreeSkillService
from src.models.database import get_db_session
from sqlalchemy.orm import Session

from src.utils.errorInjecor import *
from src.utils.errorView import ErrorView

from src.utils.crypt import hashStr, compareHash
from src.utils.sanitise import isContainsSpecialChars

from src.stats.xp import xpNeedToLvlUp


# ------>

adventurer_router = APIRouter(prefix='/adventurer', tags=['Adventurer'])
template = Jinja2Templates(directory='src/views')


# ------>

@adventurer_router.get('/createAdventurer')
def createAdventurer(
    request: Request,
    session: Session = Depends(get_db_session)
):
    """
    get page create adventurer.
    """

    resetError(request.session)

    tree_skill_service = TreeSkillService(session)

    tree_skill_class_player = tree_skill_service.getAllClassPlayer()

    reachThePage(request.session)
    return template.TemplateResponse(name='createAdventurer.html', request=request, context={
        'tree_skill_class_player': tree_skill_class_player
    })

@adventurer_router.post('/createAdventurer')
def handleCreateAdventurer(
    request: Request,
    adventurer_create_form: AdventurerCreateFormDto = Form(),
    session: Session = Depends(get_db_session)
):
    """
    create adventurer.
    """

    resetError(request.session)

    user_service = UserService(session)
    adventurer_service = AdventurerService(session)
    join_adv_tree_skill_service = JoinAdventurerTreeSkillService(session)

    user = user_service.getById(request.session.get('user', {}).get('id', -1))
    if user == None:
        
        injectError(request.session, ErrorView('user unknow'))
        injectDtoForm(request.session, adventurer_create_form)

        redirectError(request.session)
        return RedirectResponse(url='/adventurer/createAdventurer', status_code=303)
    
    # check if create over amount allow.
    adventurer_created_count = len(list(adventurer_service.getAllByUser(user.id)))
    if adventurer_created_count >= user.adventurer_allow:
        
        injectError(request.session, ErrorView('user has reach max adventurer allow'))
        injectDtoForm(request.session, adventurer_create_form)

        redirectError(request.session)
        return RedirectResponse(url='/adventurer/createAdventurer', status_code=303)
    
    adventurer_pseudo = adventurer_create_form.pseudo

    # check specail char (for html injection) and space (for regex on log during battle anime).
    if isContainsSpecialChars(adventurer_pseudo, ['<', '>', '&', ' ']):
        
        injectError(request.session, ErrorView('no space or special chars', input_name='pseudo'))
        injectDtoForm(request.session, adventurer_create_form)

        redirectError(request.session)
        return RedirectResponse(url='/adventurer/createAdventurer', status_code=303)

    # check pseudo free.
    adventurer = adventurer_service.getByPseudo(adventurer_pseudo)
    if adventurer != None:
        
        injectError(request.session, ErrorView('pseudo already used by someone else', input_name='pseudo'))
        injectDtoForm(request.session, adventurer_create_form)

        redirectError(request.session)
        return RedirectResponse(url='/adventurer/createAdventurer', status_code=303)

    # create adventurer.
    adventurer = Adventurer(
        id_user=user.id,
        pseudo=adventurer_pseudo
    )

    try:
        adventurer_service.create(adventurer)
    except Exception as e:
        session.rollback()
        
        injectError(request.session, ErrorView('an error raise from the database'))
        injectDtoForm(request.session, adventurer_create_form)
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/createAdventurer', status_code=303)
    
    # verify if tree skill is valid.
    tree_skill_id = adventurer_create_form.tree_skill
    if not TreeSkillService.isClassPlayer(tree_skill_id):  # check if tree selected is valid.
        session.rollback()
        
        injectError(request.session, ErrorView('tree skill invalid', input_name='tree_skill'))
        injectDtoForm(request.session, adventurer_create_form)
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/createAdventurer', status_code=303)

    # create join tree-skill.
    try:
        join_adv_tree_skill_service.create(JoinAdventurerTreeSkill(
            id_adventurer=adventurer.id,
            id_tree_skill=tree_skill_id
        ))
    except Exception as e:
        session.rollback()
        
        injectError(request.session, ErrorView('an error ocure during DB asignement tree skill'))
        injectDtoForm(request.session, adventurer_create_form)
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/createAdventurer', status_code=303)


    redirectError(request.session)
    return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)

# ------>

@adventurer_router.get('/listAdventurerLog')
def listAdventurerLog(
    request: Request,
    session: Session = Depends(get_db_session)
):
    """
    show all adventurer of user log.
    """

    resetError(request.session)

    adventurer_service = AdventurerService(session)

    user_id = request.session.get('user', {}).get('id', -1)
    list_adventurer = adventurer_service.getAllByUser(user_id)

    # error no user log.
    if user_id == -1:
        injectError(request.session, ErrorView('no user log'))

    reachThePage(request.session)
    return template.TemplateResponse(name='listAdventurerLog.html', request=request, context={
        'adventurers': list(list_adventurer)
    })

# ------>

@adventurer_router.get('/delete/{adventurer_id}')
def deleteAdventurer(
    request: Request,
    adventurer_id: int,
    session: Session = Depends(get_db_session)
):
    """
    delete an adventurer.
    """

    resetError(request.session)

    adventurer_service = AdventurerService(session)

    adventurer = adventurer_service.getById(adventurer_id)

    # if not found.
    if adventurer == None:
        
        injectError(request.session, ErrorView('adventurer not found'))
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)
    
    user_id = request.session.get('user', {}).get('id', None)

    # if no user log.
    if user_id == None:
        
        injectError(request.session, ErrorView('no user log'))
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)
    
    # if not own by user log.
    if user_id != adventurer.id_user:
        
        injectError(request.session, ErrorView('user log do not own the adventurer'))
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)

    # try delete.
    try:
        adventurer_service.delete(adventurer)
    except Exception as e:
        session.rollback()
    
        injectError(request.session, ErrorView('an error raise from the database'))
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)

    redirectError(request.session)
    return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)

# ------>

@adventurer_router.get('/details/{adventurer_id}')
def detailsAdventurer(
    request: Request,
    adventurer_id: int,
    session: Session = Depends(get_db_session)
):
    """
    page details about an adventurer.
    """

    adventurer_service = AdventurerService(session)

    adventurer = adventurer_service.getById(adventurer_id)
    if adventurer == None:
    
        injectError(request.session, ErrorView('adventurer not found'))
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)

    reachThePage(request.session)
    return template.TemplateResponse(name='detailsAdventurer.html', request=request, context={
        'adventurer': adventurer,
        'xp_need': xpNeedToLvlUp(adventurer.lvl)
    })