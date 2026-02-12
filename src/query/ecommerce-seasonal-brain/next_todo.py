import json
import chromadb
from chromadb.config import Settings
from datetime import datetime, timedelta

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("ecommerce_events")

today = datetime.now().date()

results = collection.get()

todos_today = []

for doc in results["documents"]:
    event = json.loads(doc)
    event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()

    for key, tasks in event["lead_times"].items():
        weeks = int(key.split("_")[0])
        target_date = event_date - timedelta(weeks=weeks)

        if target_date == today:
            todos_today.append({
                "event": event["name"],
                "tasks": tasks
            })

if not todos_today:
    print("Heute stehen keine spezifischen saisonalen Aufgaben an.")
else:
    for entry in todos_today:
        print(f"Heute fällig für {entry['event']}:")
        for t in entry["tasks"]:
            print(" -", t)