import json
import chromadb
from chromadb.config import Settings
from datetime import datetime, timedelta

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("ecommerce_events")

today = datetime.now().date()

results = collection.get()

upcoming = []

for doc in results["documents"]:
    event = json.loads(doc)
    event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()

    for key, tasks in event["lead_times"].items():
        weeks = int(key.split("_")[0])
        target_date = event_date - timedelta(weeks=weeks)
        diff = (target_date - today).days

        if diff >= 0:
            upcoming.append({
                "event": event["name"],
                "event_date": event["date"],
                "target_date": target_date.isoformat(),
                "days_until": diff,
                "tasks": tasks
            })

if not upcoming:
    print("Es stehen keine zukünftigen To-Dos an.")
else:
    upcoming_sorted = sorted(upcoming, key=lambda x: x["days_until"])
    next_item = upcoming_sorted[0]

    print(f"Nächstes To-Do für {next_item['event']}:")
    print(f"Fällig am: {next_item['target_date']} (in {next_item['days_until']} Tagen)")
    print("Aufgaben:")
    for t in next_item["tasks"]:
        print(" -", t)
