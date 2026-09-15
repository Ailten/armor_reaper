

from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates

from src.dto.battleDto import *
from fastapi.responses import RedirectResponse

from src.services.adventurerService import AdventurerService
from src.models.database import get_db_session
from sqlalchemy.orm import Session

from src.utils.errorInjecor import *
from src.utils.errorView import ErrorView

from src.utils.crypt import hashStr, compareHash
from src.utils.sanitise import htmlSanitise

from src.stats.xp import xpNeedToLvlUp

from src.stats.character import Character
from src.stats.battle import Battle
from src.stats.mobs import mobsIdToCharacter
from src.stats.treeSkills import *

# ------>

battle_router = APIRouter(prefix='/battle', tags=['Battle'])
template = Jinja2Templates(directory='src/views')


# ------>

@battle_router.get('/simulateBattle')
def createAdventurer(
    request: Request,
    start_battle_dto: StartBattleDto,
    session: Session = Depends(get_db_session)
):
    """
    return a dict of battle simulation.
    """

    adventurer_service = AdventurerService(session)

    # checks amount of adventurers.
    if len(start_battle_dto.adventurers_id) < 1 or len(start_battle_dto.adventurers_id) > 3:
    
        injectError(request.session, ErrorView('adventurers selected for battle is not rigth amount'))
        if 'adventurers_to_battle' in request.session:
            del request.session['adventurers_to_battle']
        
        redirectError(request.session)
        return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)
    
    user_id = request.session.get('user', {}).get('id', None)

    battle = Battle()

    # inject adventurer in battle.
    for adventurer_id in start_battle_dto.adventurers_id:
        adventurer = adventurer_service.getById(adventurer_id)

        # one adventurer is not found.
        if adventurer == None:
    
            injectError(request.session, ErrorView('an adventurer selected is not found'))
            if 'adventurers_to_battle' in request.session:
                del request.session['adventurers_to_battle']

            redirectError(request.session)
            return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)
        
        # if not own by user log.
        if user_id != adventurer.id_user:
        
            injectError(request.session, ErrorView('user log do not own the adventurer'))
        
            redirectError(request.session)
            return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)
        
        # cast Adventurer model into Character.
        adventurer_character = Character(vars(adventurer))

        # TODO: inject skillsTree (based on adventurer model).
        mercenaryTree(adventurer_character)

        # inject.
        battle.spawn(adventurer_character, is_left_team=True)

    # inject mobs in battle.
    for mob_id in start_battle_dto.mobs_id:
        mob_character = mobsIdToCharacter(mob_id)

        if mob_character == None:
        
            injectError(request.session, ErrorView('a mob is not found'))
        
            redirectError(request.session)
            return RedirectResponse(url='/adventurer/listAdventurerLog', status_code=303)
        
        # inject.
        battle.spawn(mob_character, is_left_team=False)

    # simulate fight.
    battle.simulateFight()

    reachThePage(request.session)
    return template.TemplateResponse(name='battle.html', request=request, context={
        'battle_logs': battle.logs,
        'battle_is_left_win': battle.is_left_win == True
    })
