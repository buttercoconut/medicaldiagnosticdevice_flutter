"""Diagnostic service layer."""
from sqlalchemy.orm import Session
from ..models.diagnostic import DiagnosticDataCreate, DiagnosticDataRead
from ..database import DiagnosticData

def create_diagnostic(db: Session, data_in: DiagnosticDataCreate) -> DiagnosticDataRead:
    db_data = DiagnosticData(**data_in.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return DiagnosticDataRead.from_orm(db_data)

def list_diagnostics(db: Session):
    return db.query(DiagnosticData).all()
