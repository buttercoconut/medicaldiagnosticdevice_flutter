"""Pydantic models for diagnostic data."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class DiagnosticData(BaseModel):
    data_id: str = Field(..., description="Unique data identifier")
    patient_id: str = Field(..., description="Reference to patient")
    timestamp: datetime = Field(..., description="Data collection timestamp")
    sensor_type: str = Field(..., description="Type of sensor (e.g., ECG, SpO2)")
    raw_values: List[float] = Field(..., description="Raw sensor readings")
    # Encrypted field for raw data if needed
    encrypted_raw: Optional[str] = Field(None, description="Encrypted raw data")

    class Config:
        orm_mode = True
