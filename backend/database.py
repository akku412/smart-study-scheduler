
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

ENGINE = create_engine('sqlite:///study_scheduler.db', echo=True)
Base.metadata.create_all(ENGINE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # <- this line imports Base

DATABASE_URL = "sqlite:///./smartstudy.db"

ENGINE = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# Create all tables
Base.metadata.create_all(bind=ENGINE)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
