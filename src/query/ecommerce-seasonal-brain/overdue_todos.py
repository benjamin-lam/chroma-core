import json
import chromadb
from chromadb.config import Settings
from datetime import datetime, timedelta

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
collection = client.get_or_create_collection("ecommerce_events")

today = datetime.now().date()

results = collection.get()

overdue = []

for doc in results["documents"]:
    event = json.loads(doc)
    event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()

    for key, tasks in event["lead_times"].items():
        weeks = int(key.split("_")[0])
        target_date = event_date - timedelta(weeks=weeks)

        if target_date < today:
            overdue.append({
                "event": event["name"],
                "event_date": event["date"],
                "target_date": target_date.isoformat(),
                "days_overdue": (today - target_date).days,
                "tasks": tasks
            })

if not overdue:
    print("Es gibt keine überfälligen Aufgaben.")
else:
    overdue_sorted = sorted(overdue, key=lambda x: x["days_overdue"])
    print("Überfällige Aufgaben:\n")
    for entry in overdue_sorted:
        print(f"{entry['event']} – war fällig am {entry['target_date']} ({entry['days_overdue']} Tage überfällig):")
        for t in entry["tasks"]:
            print(" -", t)
        print()
