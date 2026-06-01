"""Report Pydantic models."""
from pydantic import BaseModel, Field
from datetime import datetime

class ReportBase(BaseModel):
    patient_id: str
    created_at: datetime
    summary: str
    findings: str

class ReportCreate(ReportBase):
    pass

class ReportRead(ReportBase):
    id: int
    class Config:
        orm_mode = True
