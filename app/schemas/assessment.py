from pydantic import BaseModel, Field

class AssessmentBase(BaseModel):
    title: str = Field(..., example="Avaliação Final")
    course_id: int = Field(..., example=1)

class AssessmentCreate(AssessmentBase):
    pass

class AssessmentSchema(AssessmentBase):
    id: int

    class Config:
        orm_mode = True