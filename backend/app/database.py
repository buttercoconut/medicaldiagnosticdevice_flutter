"""Database models and session."""
from sqlalchemy import Column, Integer, String, Date, DateTime, JSON, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True, index=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)

class DiagnosticData(Base):
    __tablename__ = "diagnostics"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    sensor_type = Column(String)
    values = Column(JSON)

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    summary = Column(String)
    findings = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)
