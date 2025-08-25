from sqlalchemy import Column, Integer, String
from app.database import Base

class Marca(Base):
    __tablename__ = "marca"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    titular = Column(String, index=True, nullable=False)
    estado = Column(String, index=True, nullable=False)