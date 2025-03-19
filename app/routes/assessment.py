from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.assessment import Assessment
from app.schemas.assessment import AssessmentSchema, AssessmentCreate

router = APIRouter()

@router.post("/", response_model=AssessmentSchema)
def create_assessment(assessment: AssessmentCreate, db: Session = Depends(get_db)):
    db_assessment = Assessment(**assessment.dict())
    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)
    return db_assessment

@router.get("/{assessment_id}", response_model=AssessmentSchema)
def read_assessment(assessment_id: int, db: Session = Depends(get_db)):
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return assessment

@router.get("/list", response_model=list[AssessmentSchema])  # Rota alterada
def read_assessments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    assessments = db.query(Assessment).offset(skip).limit(limit).all()
    return assessments