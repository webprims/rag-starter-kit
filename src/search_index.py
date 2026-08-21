import chromadb

from ollama_helpers import embed_text

DB_PATH = "chroma_db"
COLLECTION_NAME = "webprims_knowledge"


def search(query: str, n_results: int = 3) -> list[str]:
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection(COLLECTION_NAME)

    result = collection.query(
        query_embeddings=[embed_text(query)],
        n_results=n_results,
    )

    return result["documents"][0]


if __name__ == "__main__":
    question = input("Search: ").strip()

    for i, document in enumerate(search(question), start=1):
        print(f"\nResult {i}:\n{document}")
