

from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates

from src.dto.battleDto import *
from fastapi.responses import RedirectResponse

from src.services.adventurerService import AdventurerService
from src.services.treeSkillService import TreeSkillService
from src.models.database import get_db_session
from sqlalchemy.orm import Session

from src.models.adventurer import Adventurer

from src.utils.errorInjecor import *
from src.utils.errorView import ErrorView

from src.utils.crypt import hashStr, compareHash
from src.utils.sanitise import htmlSanitise

from src.stats.character import Character
from src.stats.battle import Battle
from src.stats.mobs import mobsIdToCharacter
from src.stats.treeSkills import *
from src.stats.treeSkill import injectTreeSkill
from src.stats.xp import xpNeedToLvlUp

# ------>

battle_router = APIRouter(prefix='/battle', tags=['Battle'])
template = Jinja2Templates(directory='src/views')


# ------>

@battle_router.post('/simulateBattle')
def simulateBattle(
    request: Request,
    start_battle_dto: StartBattleDto = Form(),
    session: Session = Depends(get_db_session)
):
    """
    return a dict of battle simulation.
    """

    adventurer_service = AdventurerService(session)
    tree_skill_service = TreeSkillService(session)

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
    adventurer_models: list[Adventurer] = []
    for adventurer_id in start_battle_dto.adventurers_id:
        adventurer = adventurer_service.getById(adventurer_id)
        adventurer_models.append(adventurer)

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

        # inject tree skills.
        tree_skills = tree_skill_service.getByAdventurer(adventurer.id)
        for tree_skill in tree_skills:
            injectTreeSkill(adventurer_character, tree_skill.id)

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

    # loot, gold, and xp.
    if battle.is_left_win == True:

        # get structur of data (character, adventurer, model).
        adventurer_characters = battle.getWinnerCharacter()
        adventurer_models_match = [ next(
            [ cm for cm in adventurer_models if (
                ac.name == cm.pseudo  # get by match pseudo.
            )].__iter__()
        ) for ac in adventurer_characters ]

        # get xp data.
        total_xp = sum([ m.xp for m in battle.getLooserCharacter() ])
        split_xp = total_xp // len(adventurer_characters)

        # xp.
        for adv_i in range(len(adventurer_models_match)):
            adventurer_model = adventurer_models_match[adv_i]

            adventurer_model.xp += split_xp
            xp_need_to_lvl_up = xpNeedToLvlUp(adventurer_model.lvl)
            while adventurer_model.xp >= xp_need_to_lvl_up:  # loop lvl up.
                adventurer_model.xp -= xp_need_to_lvl_up
                adventurer_model.lvl += 1
                xp_need_to_lvl_up = xpNeedToLvlUp(adventurer_model.lvl)
    
            # save adventurer.
            try:
                adventurer_service.update(adventurer_model)
            except Exception as e:
                injectError(request.session, ErrorView('an adventurer has ocur an error to saving progression'))


        # TODO: loot and gold.

    # build character type for frontend.
    left_team = [ CharacterDto.castFromCharacter(c).model_dump() for c in battle.characters if c.is_left_team ]
    right_team = [ CharacterDto.castFromCharacter(c).model_dump() for c in battle.characters if not c.is_left_team ]

    reachThePage(request.session)
    return template.TemplateResponse(name='battle.html', request=request, context={
        'battle_logs': battle.logs,
        'left_team': left_team,
        'right_team': right_team
    })
