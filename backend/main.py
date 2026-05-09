"""Main entry point for the FastAPI application.

This module sets up the FastAPI app, includes routers, configures middleware
and provides a simple health‑check endpoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import Settings
from .api.diagnostic import router as diagnostic_router

# Load settings (environment variables)
settings = Settings()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS configuration – allow all origins for demo purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(diagnostic_router, prefix="/api/diagnostics", tags=["diagnostics"])

@app.get("/health", tags=["health"])
async def health_check():
    """Simple health‑check endpoint.

    Returns a JSON object with status and the current time.
    """
    return {"status": "ok"}

# If this module is executed directly, run the app with uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
