
from pydantic import BaseModel

class AdventurerCreateFormDto(BaseModel):
    pseudo: str
    tree_skill: int