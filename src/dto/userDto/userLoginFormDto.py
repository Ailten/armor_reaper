
from pydantic import BaseModel

class UserLoginFormDto(BaseModel):
    e_mail: str
    password: str