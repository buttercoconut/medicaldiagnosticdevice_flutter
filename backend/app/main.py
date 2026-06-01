"""FastAPI application entry point."""
from fastapi import FastAPI
from .api import patient as patient_api, diagnostic as diagnostic_api, report as report_api

app = FastAPI(title="Medical Diagnostic Device API")

app.include_router(patient_api.router)
app.include_router(diagnostic_api.router)
app.include_router(report_api.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Diagnostic Device API"}
