from typing import Optional
from pydantic import BaseModel as SCBaseModel

class WilsonSchema(SCBaseModel):
    id: Optional[int] = None
    nome = str
    especialidade = str
    foto = str
    poder = str
    

class Config:
    orm_mode = True
    