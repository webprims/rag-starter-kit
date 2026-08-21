from pathlib import Path


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 80) -> list[str]:
    """Split text into overlapping character chunks."""
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    path = Path("data/sample_knowledge.txt")
    text = path.read_text(encoding="utf-8")

    for index, chunk in enumerate(chunk_text(text), start=1):
        print(f"\n--- Chunk {index} ---\n{chunk}")
