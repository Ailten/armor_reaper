
from pydantic import BaseModel

class UserSessionDto(BaseModel):
    id: int
    e_mail: str
    pseudo: str