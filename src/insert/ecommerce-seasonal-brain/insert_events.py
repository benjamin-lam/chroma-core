import json
import chromadb
from chromadb.config import Settings
from datetime import datetime

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("ecommerce_events")

with open("data/ecommerce-seasonal-brain/events.json", "r", encoding="utf-8") as f:
    events = json.load(f)

for event in events:
    collection.add(
        ids=[event["id"]],
        documents=[json.dumps(event, ensure_ascii=False)],
        metadatas=[{
            "name": event["name"],
            "date": event["date"]
        }]
    )

print(f"Inserted {len(events)} events.")