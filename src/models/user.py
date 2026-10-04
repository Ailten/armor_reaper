
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text

from .database import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    e_mail: Mapped[str]
    password: Mapped[str]
    pseudo: Mapped[str]

    adventurer_allow: Mapped[int] = mapped_column(server_default=text('3'))
    gold: Mapped[int] = mapped_column(server_default=text('0'))
    energy: Mapped[int] = mapped_column(server_default=text('10'))
    energy_max: Mapped[int] = mapped_column(server_default=text('10'))