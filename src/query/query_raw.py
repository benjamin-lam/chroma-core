import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("sample")

results = collection.query(
    query_texts=["Beispiel"],
    n_results=3
)

print(results)