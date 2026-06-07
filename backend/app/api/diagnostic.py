"""API routes for diagnostic data."""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from datetime import datetime

from app.models.diagnostic_data import DiagnosticData
from app.services.diagnostic_service import DiagnosticService

router = APIRouter()

# Dependency injection for service
async def get_service() -> DiagnosticService:
    return DiagnosticService()

@router.post("/", response_model=DiagnosticData)
async def create_diagnostic(data: DiagnosticData, service: DiagnosticService = Depends(get_service)):
    try:
        return await service.create(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/", response_model=List[DiagnosticData])
async def list_diagnostics(patient_id: str, start: datetime, end: datetime, service: DiagnosticService = Depends(get_service)):
    return await service.list(patient_id, start, end)
