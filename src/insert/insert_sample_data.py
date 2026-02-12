import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("sample")

collection.add(
    ids=["sample_1"],
    documents=["Dies ist ein Beispiel-Dokument für die Baseline."],
    metadatas=[{"type": "sample"}]
)

print("Inserted sample data.")