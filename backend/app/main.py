"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.diagnostic import router as diagnostic_router

app = FastAPI(title="Medical Diagnostic Device API")

# CORS policy for mobile app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(diagnostic_router, prefix="/api/diagnostic", tags=["diagnostic"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Medical Diagnostic Device API"}
