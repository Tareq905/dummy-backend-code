from fastapi import APIRouter
from app.services.file_scanner import scan_folder
from app.config.settings import FOLDERS

router = APIRouter()


@router.get("/")
def get_documents():
    folder = FOLDERS.get("documents")

    if not folder or not folder.exists():
        return {
            "count": 0,
            "items": [],
            "warning": "documentFolder not found"
        }

    items = scan_folder(folder, "documentFolder")

    return {
        "count": len(items),
        "items": items
    }
