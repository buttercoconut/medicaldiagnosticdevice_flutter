"""Report service layer."""
from sqlalchemy.orm import Session
from ..models.report import ReportCreate, ReportRead
from ..database import Report

def create_report(db: Session, report_in: ReportCreate) -> ReportRead:
    db_report = Report(**report_in.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return ReportRead.from_orm(db_report)

def list_reports(db: Session):
    return db.query(Report).all()
