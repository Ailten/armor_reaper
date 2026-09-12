
from .service import Service

from sqlalchemy import select

from src.models.user import User


class UserService(Service):

    def getByEMail(self, user_e_mail: str) -> User|None:
        return self.session.scalar(
            select(User).where(User.e_mail == user_e_mail)
        )

    def getByPseudo(self, pseudo: str) -> User|None:
        return self.session.scalar(
            select(User).where(User.pseudo == pseudo)
        )