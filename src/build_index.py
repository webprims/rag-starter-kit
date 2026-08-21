from pathlib import Path

import chromadb

from chunk_text import chunk_text
from ollama_helpers import embed_text

DB_PATH = "chroma_db"
COLLECTION_NAME = "webprims_knowledge"


def main() -> None:
    text = Path("data/sample_knowledge.txt").read_text(encoding="utf-8")
    chunks = chunk_text(text)

    client = chromadb.PersistentClient(path=DB_PATH)

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(COLLECTION_NAME)

    embeddings = [embed_text(chunk) for chunk in chunks]
    ids = [f"chunk-{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )

    print(f"Indexed {len(chunks)} chunks into {DB_PATH}/{COLLECTION_NAME}")


if __name__ == "__main__":
    main()
