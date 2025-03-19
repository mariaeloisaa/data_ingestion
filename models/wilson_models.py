from core.configs import settings
from sqlalchemy import Column, Integer, String

class WilsonModel(settings.DBBaseModel):
    __tablename_ = "WilsonVerso"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(256))
    especialidade: str = Column(String(256))
    poder: str = Column(String(256))
    foto: str = Column(String(256))