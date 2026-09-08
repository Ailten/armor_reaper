
from sqlalchemy.orm import Mapped, mapped_column

from .database import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    e_mail: Mapped[str]
    password: Mapped[str]
    pseudo: Mapped[str]