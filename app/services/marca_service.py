from sqlalchemy.orm import Session
from app.models.marca_model import Marca
from app.schemas.marca_schema import MarcaRegistrar

def get_marca(db: Session, marca_id: int):
    return db.query(Marca).filter(Marca.id == marca_id).first()

def get_marcas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Marca).offset(skip).limit(limit).all()

def registrar_marca(db: Session, marca: MarcaRegistrar):
    db_marca = Marca(
        nombre=marca.nombre,
        titular=marca.titular,
        estado=marca.estado
    )
    db.add(db_marca)
    db.commit()
    db.refresh(db_marca)
    return db_marca

def eliminar_marca(db: Session, marca_id: int):
    marca = db.query(Marca).filter(Marca.id == marca_id).first()
    if marca:
        db.delete(marca)
        db.commit()
        return True
    return False

def actualizar_marca(db: Session, marca_id: int, marca_data: MarcaRegistrar):
    marca = db.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        return None
    marca.nombre = marca_data.nombre
    marca.titular = marca_data.titular
    marca.estado = marca_data.estado
    db.commit()
    db.refresh(marca)
    return marca

