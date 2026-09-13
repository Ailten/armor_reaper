
from pydantic import BaseModel

class UserSessionDto(BaseModel):
    id: int
    pseudo: str

    adventurer_allow: int
    gold: int
    energy: int
    energy_max: int

# ------>

from src.models.user import User

def castUserAsSessionDto(user: User) -> UserSessionDto:
    return UserSessionDto(
        id=user.id,
        pseudo=user.pseudo,

        adventurer_allow=user.adventurer_allow,
        gold=user.gold,
        energy=user.energy,
        energy_max=user.energy_max
    )