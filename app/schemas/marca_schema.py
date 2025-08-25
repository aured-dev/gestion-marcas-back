from pydantic import BaseModel

class MarcaBase(BaseModel):
    nombre: str
    titular: str
    estado: str

class MarcaRegistrar(MarcaBase):
    pass

class Marca(MarcaBase):
    id: int

    class Config:
        orm_mode = True
