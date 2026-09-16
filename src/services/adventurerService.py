
from .service import Service

from sqlalchemy import select

from src.models.adventurer import Adventurer


class AdventurerService(Service):

    def getByPseudo(self, adventurer_pseudo: str) -> Adventurer|None:
        return self.session.scalar(
            select(Adventurer).where(Adventurer.pseudo == adventurer_pseudo)
        )
    
    def getById(self, adventurer_id: int) -> Adventurer|None:
        return self.session.scalar(
            select(Adventurer).where(Adventurer.id == adventurer_id)
        )
    
    def getAllByUser(self, user_id: int) -> list[Adventurer]:
        return self.session.scalars(
            select(Adventurer).where(Adventurer.id_user == user_id)
        ).all()
    