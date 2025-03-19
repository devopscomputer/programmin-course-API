from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.module import Module
from app.schemas.module import ModuleSchema, ModuleCreate

router = APIRouter()

@router.post("/", response_model=ModuleSchema)
def create_module(module: ModuleCreate, db: Session = Depends(get_db)):
    db_module = Module(**module.dict())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module

@router.get("/{module_id}", response_model=ModuleSchema)
def read_module(module_id: int, db: Session = Depends(get_db)):
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return module

@router.get("/list", response_model=list[ModuleSchema])  # Rota alterada
def read_modules(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    modules = db.query(Module).offset(skip).limit(limit).all()
    return modules