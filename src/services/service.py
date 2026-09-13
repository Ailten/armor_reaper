
from abc import ABC

from sqlalchemy.orm import Session

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.database import BaseModel

class Service(ABC):

    def __init__(self, session: Session):
        self.session = session

    def create(self, model: "BaseModel"):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

    def delete(self, model: "BaseModel"):
        self.session.delete(model)
        self.session.commit()

    