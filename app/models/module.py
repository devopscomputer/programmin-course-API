from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base

class Module(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course", back_populates="modules")