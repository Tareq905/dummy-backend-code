from typing import List, Dict, Any, Optional


def normalize_items(
    raw_items: List[Any],
    item_type: str,
    source: str,
    confidence: Optional[float] = None
) -> List[Dict]:
    """
    Normalizes raw AI-extracted items into a stable schema.

    Args:
        raw_items (List[Any]): Raw outputs from AI (strings or dicts)
        item_type (str): One of: task, risk, issue, decision, action, assumption
        source (str): Source name (email, meeting, document, etc.)
        confidence (Optional[float]): Optional confidence score

    Returns:
        List[Dict]: Normalized items
    """

    normalized = []

    if not raw_items:
        return normalized

    for idx, item in enumerate(raw_items):
        if not item:
            continue

        if isinstance(item, str):
            text = item.strip()
            metadata = {}

        elif isinstance(item, dict):
            text = str(item.get("text", "")).strip()
            metadata = {
                k: v for k, v in item.items() if k != "text"
            }

        else:
            # Unsupported type → skip safely
            continue

        if not text:
            continue

        normalized.append({
            "id": f"{item_type}_{idx}",
            "type": item_type,
            "text": text,
            "source": source,
            "confidence": confidence,
            "metadata": metadata
        })

    return normalized
