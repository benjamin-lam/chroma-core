import json
import chromadb
from chromadb.config import Settings
from datetime import datetime, timedelta

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("ecommerce_events")

today = datetime.now().date()
end_of_week = today + timedelta(days=7)

results = collection.get()

todos = []

for doc in results["documents"]:
    event = json.loads(doc)
    event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()

    for key, tasks in event["lead_times"].items():
        weeks = int(key.split("_")[0])
        target_date = event_date - timedelta(weeks=weeks)

        if today <= target_date <= end_of_week:
            todos.append({
                "event": event["name"],
                "event_date": event["date"],
                "target_date": target_date.isoformat(),
                "tasks": tasks
            })

if not todos:
    print("Diese Woche stehen keine saisonalen Aufgaben an.")
else:
    print("To-Dos für diese Woche:\n")
    for entry in todos:
        print(f"{entry['event']} – fällig am {entry['target_date']}:")
        for t in entry["tasks"]:
            print(" -", t)
        print()
