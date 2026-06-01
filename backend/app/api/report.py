"""FastAPI routers for reports."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.report import ReportCreate, ReportRead
from ..services.report_service import create_report, list_reports
from ..dependencies import get_db

router = APIRouter(prefix="/reports", tags=["reports"])

@router.post("/", response_model=ReportRead, status_code=status.HTTP_201_CREATED)
def api_create_report(report: ReportCreate, db: Session = Depends(get_db)):
    return create_report(db, report)

@router.get("/", response_model=List[ReportRead])
def api_list_reports(db: Session = Depends(get_db)):
    return list_reports(db)
