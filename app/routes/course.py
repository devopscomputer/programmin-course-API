from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.course import Course
from app.schemas.course import CourseSchema, CourseCreate

router = APIRouter()

@router.post("/", response_model=CourseSchema)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/{course_id}", response_model=CourseSchema)
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/list", response_model=list[CourseSchema])  # Rota alterada
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses