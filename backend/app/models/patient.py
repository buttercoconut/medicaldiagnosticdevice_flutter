"""Pydantic models for patient data."""
from pydantic import BaseModel, Field
from datetime import datetime

class Patient(BaseModel):
    patient_id: str = Field(..., description="Unique patient identifier")
    name: str = Field(..., description="Patient full name")
    date_of_birth: datetime = Field(..., description="Date of birth")
    gender: str = Field(..., description="Gender (M/F/Other)")
    # Sensitive fields can be encrypted at rest
    ssn: str = Field(..., description="Encrypted SSN")

    class Config:
        orm_mode = True
