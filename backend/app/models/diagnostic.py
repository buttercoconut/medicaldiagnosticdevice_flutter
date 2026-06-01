"""Diagnostic data Pydantic models."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict

class DiagnosticDataBase(BaseModel):
    patient_id: str
    timestamp: datetime
    sensor_type: str
    values: Dict[str, float]  # e.g., {"heart_rate": 72}

class DiagnosticDataCreate(DiagnosticDataBase):
    pass

class DiagnosticDataRead(DiagnosticDataBase):
    id: int
    class Config:
        orm_mode = True
