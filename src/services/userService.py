
from .service import Service

from sqlalchemy import select, update

from src.models.user import User


class UserService(Service):

    def getByEMail(self, user_e_mail: str) -> User|None:
        return self.session.scalar(
            select(User).where(User.e_mail == user_e_mail)
        )

    def getByPseudo(self, user_pseudo: str) -> User|None:
        return self.session.scalar(
            select(User).where(User.pseudo == user_pseudo)
        )
    
    def getById(self, user_id: int) -> User|None:
        return self.session.scalar(
            select(User).where(User.id == user_id)
        )
    
    def refillEnergy(self):
        self.session.execute(
            update(User)
            .where(User.energy < User.energy_max)
            .values(energy = User.energy_max)
        )