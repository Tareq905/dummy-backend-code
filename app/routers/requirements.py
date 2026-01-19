from fastapi import APIRouter
from app.services.file_scanner import scan_folder
from app.config.settings import FOLDERS

router = APIRouter()


@router.get("/")
def get_requirements():
    folder = FOLDERS.get("requirements")

    if not folder or not folder.exists():
        return {
            "count": 0,
            "items": [],
            "warning": "requirements folder not found"
        }

    items = scan_folder(folder, "requirements")

    return {
        "count": len(items),
        "items": items
    }
