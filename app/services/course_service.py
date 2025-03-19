from sqlalchemy.orm import Session
from app.models.course import Course
from app.schemas.course import CourseCreate

class CourseService:
    def __init__(self, db: Session):
        self.db = db

    def create_course(self, course: CourseCreate) -> Course:
        db_course = Course(**course.dict())
        self.db.add(db_course)
        self.db.commit()
        self.db.refresh(db_course)
        return db_course

    def get_course(self, course_id: int) -> Course:
        return self.db.query(Course).filter(Course.id == course_id).first()

    def get_courses(self, skip: int = 0, limit: int = 10) -> list[Course]:
        return self.db.query(Course).offset(skip).limit(limit).all()