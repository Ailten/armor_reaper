
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text

from .database import BaseModel

class Adventurer(BaseModel):
    __tablename__ = 'adventurers'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int]
    pseudo: Mapped[str]

    lvl: Mapped[int] = mapped_column(server_default=text("1"))
    xp: Mapped[int] = mapped_column(server_default=text("0"))
