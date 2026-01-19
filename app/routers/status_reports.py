from fastapi import APIRouter
from app.services.file_scanner import scan_folder
from app.config.settings import FOLDERS

router = APIRouter()


@router.get("/")
def get_status_reports():
    folder = FOLDERS.get("status_reports")

    if not folder or not folder.exists():
        return {
            "count": 0,
            "items": [],
            "warning": "statusReport folder not found"
        }

    reports = scan_folder(folder, "statusReport")

    return {
        "count": len(reports),
        "items": reports
    }
