from fastapi import APIRouter
from app.services.file_scanner import scan_folder
from app.config.settings import FOLDERS

router = APIRouter()


@router.get("/")
def get_meetings():
    folder = FOLDERS.get("meetings")

    if not folder or not folder.exists():
        return {
            "count": 0,
            "items": [],
            "warning": "meetings folder not found"
        }

    items = scan_folder(folder, "meetings")

    return {
        "count": len(items),
        "items": items
    }
