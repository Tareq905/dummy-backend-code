from fastapi import APIRouter
from app.services.file_scanner import scan_folder
from app.config.settings import FOLDERS

router = APIRouter()


@router.get("/")
def get_risks():
    folder = FOLDERS.get("risks")

    if not folder or not folder.exists():
        return {
            "count": 0,
            "items": [],
            "warning": "risks folder not found"
        }

    items = scan_folder(folder, "risks")

    return {
        "count": len(items),
        "items": items
    }
