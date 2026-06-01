"""FastAPI routers for diagnostic data."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.diagnostic import DiagnosticDataCreate, DiagnosticDataRead
from ..services.diagnostic_service import create_diagnostic, list_diagnostics
from ..dependencies import get_db

router = APIRouter(prefix="/diagnostics", tags=["diagnostics"])

@router.post("/", response_model=DiagnosticDataRead, status_code=status.HTTP_201_CREATED)
def api_create_diagnostic(data: DiagnosticDataCreate, db: Session = Depends(get_db)):
    return create_diagnostic(db, data)

@router.get("/", response_model=List[DiagnosticDataRead])
def api_list_diagnostics(db: Session = Depends(get_db)):
    return list_diagnostics(db)
