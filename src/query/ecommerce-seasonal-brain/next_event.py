import json
import chromadb
from chromadb.config import Settings
from datetime import datetime

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("ecommerce_events")

today = datetime.now().date()

results = collection.get()

closest = None
closest_diff = None

for doc, meta in zip(results["documents"], results["metadatas"]):
    event = json.loads(doc)
    event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
    diff = (event_date - today).days

    if diff >= 0 and (closest_diff is None or diff < closest_diff):
        closest = event
        closest_diff = diff

print("Nächstes Event:", closest["name"])
print("Datum:", closest["date"])
print("Tage bis dahin:", closest_diff)
