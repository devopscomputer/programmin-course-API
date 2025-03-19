from sqlalchemy.orm import Session
from app.models.module import Module
from app.schemas.module import ModuleCreate

class ModuleService:
    def __init__(self, db: Session):
        self.db = db

    def create_module(self, module: ModuleCreate) -> Module:
        db_module = Module(**module.dict())
        self.db.add(db_module)
        self.db.commit()
        self.db.refresh(db_module)
        return db_module

    def get_module(self, module_id: int) -> Module:
        return self.db.query(Module).filter(Module.id == module_id).first()

    def get_modules(self, skip: int = 0, limit: int = 10) -> list[Module]:
        return self.db.query(Module).offset(skip).limit(limit).all()