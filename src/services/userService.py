
from .service import Service

from sqlalchemy import select

from src.models.user import User


class UserService(Service):

    def getByEMail(self, user_e_mail: str) -> User|None:
        return self.session.scalar(
            select(User).where(User.e_mail == user_e_mail)
        )
    
    def create(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)