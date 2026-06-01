"""Patient service layer."""
from sqlalchemy.orm import Session
from ..models.patient import PatientCreate, PatientRead
from ..database import Patient

def create_patient(db: Session, patient_in: PatientCreate) -> PatientRead:
    db_patient = Patient(**patient_in.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return PatientRead.from_orm(db_patient)

def get_patient(db: Session, patient_id: str):
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()

def list_patients(db: Session):
    return db.query(Patient).all()
