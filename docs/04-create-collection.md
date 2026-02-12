# Persistente ChromaDB initialisieren

```python
import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="./chroma", settings=Settings())
print(client.list_collections())
```
