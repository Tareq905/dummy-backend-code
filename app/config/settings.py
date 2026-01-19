from pathlib import Path

BASE_DATA_DIR = Path("data")

FOLDERS = {
    "contracts": BASE_DATA_DIR / "contractRequirements",
    "documents": BASE_DATA_DIR / "documentFolder",
    "meetings": BASE_DATA_DIR / "meetings",
    "requirements": BASE_DATA_DIR / "requirements",
    "risks": BASE_DATA_DIR / "risks",
    "status_reports": BASE_DATA_DIR / "statusReport",
}

SUPPORTED_EXTENSIONS = {
    ".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".csv", ".png", ".jpg", ".jpeg"
}
