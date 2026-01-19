from typing import List, Dict


def chunk_text(
    text: str,
    chunk_size: int = 1500,
    overlap: int = 200
) -> List[Dict]:
    """
    Splits text into overlapping chunks.

    Args:
        text (str): Full extracted text
        chunk_size (int): Max characters per chunk
        overlap (int): Overlap between chunks (characters)

    Returns:
        List[Dict]: Ordered chunks with metadata
    """

    if not text or not text.strip():
        return []

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    index = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk_content = text[start:end]

        if chunk_content.strip():
            chunks.append({
                "chunk_index": index,
                "start_char": start,
                "end_char": min(end, text_length),
                "content": chunk_content.strip(),
                "length": len(chunk_content.strip())
            })
            index += 1

        start = end - overlap

    return chunks
