
from .service import Service

from sqlalchemy import select

from src.models.treeSkill import TreeSkill
from models.joinAdventurerTreeSkill import JoinAdventurerTreeSkill


class TreeSkillService(Service):
    __all: list[TreeSkill]|None = None
    __tree_skill_class_player: list[int] = [1,2,3]

    def __getAll(self):
        TreeSkillService.__all = list(self.session.scalar(
            select(TreeSkill)
        ))

    # ------>

    def getByName(self, name: str) -> TreeSkill|None:
        if TreeSkillService.__all == None:
            self.__getAll()

        for st in TreeSkillService.__all:
            if st.name == name:
                return st
            
        return None
    
    def getById(self, id: int) -> TreeSkill|None:
        if TreeSkillService.__all == None:
            self.__getAll()

        id -= 1
        if id < 0 or id >= len(TreeSkillService.__all):
            return None
        
        return TreeSkillService.__all[id]
        
    def getByAdventurer(self, adventurer_id: int) -> list[TreeSkill]:
        return self.session.scalars(
            select(TreeSkill)
            .join(JoinAdventurerTreeSkill, JoinAdventurerTreeSkill.id_tree_skill == TreeSkill.id)
            .where(JoinAdventurerTreeSkill.id_adventurer == adventurer_id)
        )
    
    def getAllClassPlayer(self) -> list[TreeSkill]:
        if TreeSkillService.__all == None:
            self.__getAll()
        
        return [ts for ts in TreeSkillService.__all if ts.id in TreeSkillService.__tree_skill_class_player]
    
    @staticmethod
    def isClassPlayer(tree_skill_id: int) -> bool:
        return tree_skill_id in TreeSkillService.__tree_skill_class_player
