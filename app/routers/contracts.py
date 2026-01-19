from fastapi import APIRouter
from app.services.file_scanner import scan_folder
from app.config.settings import FOLDERS

router = APIRouter()


@router.get("/")
def get_contracts():
    folder = FOLDERS.get("contracts")

    if not folder or not folder.exists():
        return {
            "count": 0,
            "items": [],
            "warning": "contracts folder not found"
        }

    items = scan_folder(folder, "contractRequirements")

    return {
        "count": len(items),
        "items": items
    }
