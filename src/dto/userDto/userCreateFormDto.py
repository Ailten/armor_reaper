
from pydantic import BaseModel

class UserCreateFormDto(BaseModel):
    e_mail: str
    password: str