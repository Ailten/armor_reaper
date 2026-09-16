
from sqlalchemy.orm import Mapped, mapped_column

from .database import BaseModel

class TreeSkill(BaseModel):
    __tablename__ = 'tree_skills'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]