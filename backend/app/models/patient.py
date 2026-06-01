"""Patient Pydantic models."""
from pydantic import BaseModel, Field
from datetime import date

class PatientBase(BaseModel):
    patient_id: str = Field(..., description="Unique patient identifier")
    name: str
    birth_date: date
    gender: str
    phone: str | None = None
    email: str | None = None

class PatientCreate(PatientBase):
    pass

class PatientRead(PatientBase):
    class Config:
        orm_mode = True
