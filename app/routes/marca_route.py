from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import marca_service
from app import schemas, database

router = APIRouter(prefix="/api/marcas", tags=["Marcas"])

@router.post("/", response_model=schemas.marca_schema.Marca)
def registrar_marca(marca: schemas.marca_schema.MarcaRegistrar, db: Session = Depends(database.get_db)):
    return marca_service.registrar_marca(db, marca)

@router.get("/", response_model=list[schemas.marca_schema.Marca])
def listar_marcas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return marca_service.get_marcas(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.marca_schema.Marca)
def obtener_marca(id: int, db: Session = Depends(database.get_db)):
    db_marca = marca_service.get_marca(db, id)
    if not db_marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_marca

@router.put("/{id}", response_model=schemas.marca_schema.Marca)
def actualizar_marca(id: int, marca: schemas.marca_schema.MarcaRegistrar, db: Session = Depends(database.get_db)):
    updated = marca_service.actualizar_marca(db, id, marca)
    if not updated:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return updated

@router.delete("/{id}")
def eliminar_marca(id: int, db: Session = Depends(database.get_db)):
    if not marca_service.eliminar_marca(db, id):
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return {"message": "Marca eliminada"}
