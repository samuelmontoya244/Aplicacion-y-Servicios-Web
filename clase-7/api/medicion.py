from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from crud import medicion as crud_medicion
from database import get_db
from schemas.medicion import MedicionCreate, MedicionResponse, MedicionUpdate

router = APIRouter(prefix="/mediciones", tags=["Mediciones"])

@router.get("", response_model=list[MedicionResponse])
def listar_mediciones(db: Session = Depends(get_db)):
    return crud_medicion.get_all(db)

@router.get("/{medicion_id}", response_model=MedicionResponse)
def obtener_mediciones(medicion_id: int, db: Session = Depends(get_db)):
    medicion = crud_medicion.get(db, medicion_id)
    if medicion is None:
        raise HTTPException(status_code=404, detail="La medición no existe")
    return medicion

@router.post("", response_model=MedicionResponse, status_code=status.HTTP_201_CREATED)
def agregar_mediciones(data: MedicionCreate, db: Session = Depends(get_db)):
    return crud_medicion.create(db, data)

@router.put("/{medicion_id}", response_model=MedicionResponse)
def reemplazar_mediciones(medicion_id: int, data: MedicionCreate, db: Session = Depends(get_db)):
    medicion = crud_medicion.get(db, medicion_id)
    if medicion is None:
        raise HTTPException(status_code=404, detail="La medición no existe")
    return crud_medicion.update(db, medicion, MedicionUpdate(**data.model_dump()))

@router.patch("/{medicion_id}", response_model=MedicionResponse)
def actualizar_mediciones(medicion_id: int, data: MedicionUpdate, db: Session = Depends(get_db)):
    medicion = crud_medicion.get(db, medicion_id)
    if medicion is None:
        raise HTTPException(status_code=404, detail="La medición no existe")
    return crud_medicion.update(db, medicion, data)


