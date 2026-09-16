
from .service import Service

from sqlalchemy import select

from src.models.treeSkill import TreeSkill
from src.models.joinAdventurersTreeSkill import JoinAdventurerTreeSkill


class TreeSkillService(Service):
    __all: list[TreeSkill]|None = None

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