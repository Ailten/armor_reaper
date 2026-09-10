
from pydantic import BaseModel

class UserSessionDto(BaseModel):
    id: int
    pseudo: str


# ------>

from src.models.user import User

def castUserAsSessionDto(user: User) -> UserSessionDto:
    return UserSessionDto(
        id=user.id,
        pseudo=user.pseudo
    )