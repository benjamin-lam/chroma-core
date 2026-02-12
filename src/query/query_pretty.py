import chromadb
from chromadb.config import Settings
from src.utils.pretty_print import pretty_print

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("sample")

results = collection.query(
    query_texts=["Beispiel"],
    n_results=3
)

pretty_print(results)