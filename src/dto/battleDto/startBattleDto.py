
from pydantic import BaseModel

class StartBattleDto(BaseModel):
    adventurers_id: list[int]
    mobs_id: list[int]