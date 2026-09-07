
from abc import ABC

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlalchemy.orm import Session

class Service(ABC):

    def __init__(self, session: Session):
        self.session = session