
from sqlalchemy.orm import Mapped, mapped_column

from .database import BaseModel

class Adventurer(BaseModel):
    __tablename__ = 'adventurers'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int]
    pseudo: Mapped[str]