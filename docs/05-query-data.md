# Daten abfragen

## Rohformat

```python
results = collection.query(
    query_texts=["Beispiel"],
    n_results=3
)
print(results)
```

### Schön formatiert

```python
from src.utils.pretty_print import pretty_print
pretty_print(results)
```