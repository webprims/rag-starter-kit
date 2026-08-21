import chromadb

from ollama_helpers import chat, embed_text

DB_PATH = "chroma_db"
COLLECTION_NAME = "webprims_knowledge"


def retrieve(question: str, n_results: int = 3) -> list[str]:
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection(COLLECTION_NAME)

    result = collection.query(
        query_embeddings=[embed_text(question)],
        n_results=n_results,
    )

    return result["documents"][0]


def answer_question(question: str) -> str:
    context_chunks = retrieve(question)
    context = "\n\n---\n\n".join(context_chunks)

    prompt = f"""You are a helpful assistant.
Answer the user's question using only the context below.
If the answer is not present in the context, say you don't know based on the provided knowledge base.

Context:
{context}

Question: {question}

Answer:"""

    return chat(prompt)


def main() -> None:
    print("Local RAG Chat — type 'exit' to quit")

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        try:
            response = answer_question(question)
            print(f"\nAssistant: {response}")
        except Exception as error:
            print(f"\nError: {error}")
            print("Make sure Ollama is running and the vector index has been built.")


if __name__ == "__main__":
    main()
