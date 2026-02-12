import json

def pretty_print(results):
    """
    Gibt ChromaDB-Query-Ergebnisse formatiert aus.
    """
    try:
        print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
    except Exception:
        print("Raw results:")
        print(results)