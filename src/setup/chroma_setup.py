import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(
    path="./chroma",
    settings=Settings(anonymized_telemetry=False),
    settings=Settings()
)

print("Collections:", client.list_collections())
