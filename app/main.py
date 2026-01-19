from fastapi import FastAPI
from app.routers import (
    contracts,
    meetings,
    requirements,
    risks,
    status_reports,
    documents
)

app = FastAPI(
    title="Temporary File Data API",
    version="0.1.0",
    description="Temporary backend for AI agents using file-based storage"
)

app.include_router(contracts.router, prefix="/contracts", tags=["Contracts"])
app.include_router(meetings.router, prefix="/meetings", tags=["Meetings"])
app.include_router(requirements.router, prefix="/requirements", tags=["Requirements"])
app.include_router(risks.router, prefix="/risks", tags=["Risks"])
app.include_router(status_reports.router, prefix="/status-reports", tags=["Status Reports"])
app.include_router(documents.router, prefix="/documents", tags=["Documents"])


@app.get("/")
def health_check():
    return {"status": "ok"}
