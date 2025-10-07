
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    energy_peak = Column(String(20))  # e.g., 'morning', 'evening'
    user_type = Column(String(20))    # e.g., 'morning_person', 'night_owl'
    created_at = Column(DateTime, default=datetime.utcnow)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(50))
    difficulty = Column(Float)  # 1-10
    exam_date = Column(DateTime)
    progress = Column(Float, default=0.0)  # 0-100%
    user = relationship("User ")

class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    start_time = Column(DateTime)
    duration = Column(Integer)  # minutes
    type = Column(String(20))   # e.g., 'reading', 'practice'
    completed = Column(Boolean, default=False)
    user = relationship("User ")
    subject = relationship("Subject")
    from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

