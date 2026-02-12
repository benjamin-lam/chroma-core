# Troubleshooting

## Fehler: ModuleNotFoundError: chromadb.api.types

Ursache: Alte ChromaDB-Version + Python 3.12

Lösung:

```bash
pip uninstall -y chromadb
pip install "chromadb>=0.5.4,<0.6.0"
```