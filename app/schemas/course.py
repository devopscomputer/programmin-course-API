from pydantic import BaseModel, Field
from typing import List, Optional

class ModuleBase(BaseModel):
    title: str = Field(..., example="Introdução ao Python")
    content: str = Field(..., example="Conteúdo do módulo")

class CourseBase(BaseModel):
    title: str = Field(..., example="Curso de Programação em Python")
    description: str = Field(..., example="Aprenda Python do básico ao avançado")
    modules: Optional[List[ModuleBase]] = None

class CourseCreate(CourseBase):
    pass

class CourseSchema(CourseBase):
    id: int

    class Config:
        orm_mode = True