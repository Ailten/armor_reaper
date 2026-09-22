
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, ForeignKey

from .database import BaseModel

class JoinAdventurerTreeSkill(BaseModel):
    __tablename__ = 'join_adventurer_tree_skills'

    id_adventurer: Mapped[int] = Column(ForeignKey('adventurers.id'), primary_key=True)
    id_tree_skill: Mapped[int] = Column(ForeignKey('tree_skills.id'), primary_key=True)