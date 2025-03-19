from pydantic import BaseModel, Field

class ModuleCreate(BaseModel):
    title: str = Field(..., example="Título do Módulo")
    content: str = Field(..., example="Conteúdo do Módulo")

class ModuleSchema(ModuleCreate):
    id: int

    class Config:
        orm_mode = True  # Se estiver usando Pydantic v2, troque por from_attributes