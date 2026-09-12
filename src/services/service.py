
from abc import ABC

from sqlalchemy.orm import Session

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.database import BaseModel

class Service(ABC):

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: "BaseModel"):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)