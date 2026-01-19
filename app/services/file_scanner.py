from pathlib import Path
from app.services.text_extractor import extract_text
import hashlib

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".pptx"}


def _generate_stable_id(file: Path) -> str:
    """
    Generates a deterministic ID based on absolute file path.
    This prevents collisions across folders and time.
    """
    raw = str(file.resolve()).encode("utf-8")
    return hashlib.md5(raw).hexdigest()


def scan_folder(folder: Path, source_name: str):
    results = []

    if not folder.exists() or not folder.is_dir():
        return results

    for file in folder.rglob("*"):
        if not file.is_file():
            continue

        suffix = file.suffix.lower()
        if suffix not in SUPPORTED_EXTENSIONS:
            continue

        try:
            content = extract_text(file)
        except Exception:
            # Skip unreadable or corrupted files safely
            continue

        if not content or not content.strip():
            continue

        stable_id = _generate_stable_id(file)

        results.append({
            # Use stable ID as primary identifier
            "id": stable_id,

            # Keep filename for UI display
            "file_name": file.name,

            # Relative path helps debugging and future migrations
            "relative_path": str(file.relative_to(folder)),

            # Source context
            "source_folder": source_name,
            "file_type": suffix,

            # Content payload
            "content": content,
            "content_length": len(content),

            # Minimal metadata (needed later by agents)
            "file_size_bytes": file.stat().st_size,
            "last_modified": file.stat().st_mtime,
        })

    return results
