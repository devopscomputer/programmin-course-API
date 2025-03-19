from sqlalchemy.orm import Session
from app.models.assessment import Assessment
from app.schemas.assessment import AssessmentCreate

class AssessmentService:
    def __init__(self, db: Session):
        self.db = db

    def create_assessment(self, assessment: AssessmentCreate) -> Assessment:
        db_assessment = Assessment(**assessment.dict())
        self.db.add(db_assessment)
        self.db.commit()
        self.db.refresh(db_assessment)
        return db_assessment

    def get_assessment(self, assessment_id: int) -> Assessment:
        return self.db.query(Assessment).filter(Assessment.id == assessment_id).first()

    def get_assessments(self, skip: int = 0, limit: int = 10) -> list[Assessment]:
        return self.db.query(Assessment).offset(skip).limit(limit).all()