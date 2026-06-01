"""FastAPI routers for patients."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.patient import PatientCreate, PatientRead
from ..services.patient_service import get_patient, create_patient, list_patients
from ..dependencies import get_db

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=PatientRead, status_code=status.HTTP_201_CREATED)
def api_create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)

@router.get("/", response_model=List[PatientRead])
def api_list_patients(db: Session = Depends(get_db)):
    return list_patients(db)

@router.get("/{patient_id}", response_model=PatientRead)
def api_get_patient(patient_id: str, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
