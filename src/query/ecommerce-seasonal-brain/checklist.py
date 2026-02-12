import json
import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("ecommerce_events")

results = collection.get()

for doc in results["documents"]:
    event = json.loads(doc)
    print(f"Checklisten für {event['name']}:")
    for category, items in event["checklists"].items():
        print(f"  {category}:")
        for item in items:
            print("   -", item)
    print()