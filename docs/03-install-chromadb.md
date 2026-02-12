# ChromaDB installieren

Reproduzierbare Installation (mit aktiver venv):

```bash
   pip install "chromadb>=0.5.4,<0.6.0"
```

Optional (empfohlen für spätere Agent‑Pipelines):
```bash
   pip install chromadb[server]
```

Persistente ChromaDB initialisieren

Erstelle eine Datei chroma_setup.py:
```python
import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(
    path="./chroma",
    settings=Settings()
)

print("Collections:", client.list_collections())

```
```bash
python chroma_setup.py
```

Version prüfen:
```bash
python -c "import chromadb; print(chromadb.__version__)"
```

Ohne venv (System-Python, z. B. Ubuntu):
```bash
python3 -c "import chromadb; print(chromadb.__version__)"
```