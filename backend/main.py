
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db, ENGINE
from ai_engine import AIEngine
from models import User, Subject, Schedule
import models  # Ensure tables created
from datetime import datetime

app = FastAPI(title="Smart Study Scheduler AI")

# ✅ Allow CORS for frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root Route
@app.get("/")
def read_root():
    return {"message": "Smart Study Scheduler Backend is running!"}

# ✅ Request Models
class UserCreate(BaseModel):
    name: str
    energy_peak: str
    user_type: str

class SubjectCreate(BaseModel):
    name: str
    difficulty: float
    exam_date: str  # ISO format

# ✅ Routes
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, energy_peak=user.energy_peak, user_type=user.user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id}

@app.post("/subjects/{user_id}")
def add_subject(user_id: int, subject: SubjectCreate, db: Session = Depends(get_db)):
    db_subject = Subject(
        user_id=user_id,
        name=subject.name,
        difficulty=subject.difficulty,
        exam_date=datetime.fromisoformat(subject.exam_date)
    )
    db.add(db_subject)
    db.commit()
    return {"id": db_subject.id}

@app.get("/schedule/{user_id}")
def get_schedule(user_id: int, db: Session = Depends(get_db)):
    engine = AIEngine(db)
    schedule = engine.generate_schedule(user_id)
    return {"schedule": schedule}

@app.post("/complete/{schedule_id}")
def mark_complete(schedule_id: int, completed: bool, db: Session = Depends(get_db)):
    engine = AIEngine(db)
    engine.mark_completion(schedule_id, completed)
    return {"status": "updated"}

@app.get("/reschedule/{user_id}")
def reschedule(user_id: int, db: Session = Depends(get_db)):
    engine = AIEngine(db)
    new_slots, message = engine.reschedule_missed(user_id)
    return {"new_slots": new_slots, "message": message}

# ✅ Run Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
