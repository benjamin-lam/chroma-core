# 📘 **README.md**

# Chroma Core – Baseline Setup für eine lokale Wissensdatenbank

Dieses Repository stellt eine neutrale, erweiterbare Baseline bereit,
um eine lokale ChromaDB als Wissensbasis aufzusetzen.  
Es dient als Grundlage für Feature-Branches wie:

- E-Commerce Seasonal Brain
- Project Truth
- Agent Knowledge Base
- uvm.

Der Fokus liegt auf:

- Reproduzierbarkeit
- Klarer Struktur
- Erweiterbarkeit
- Didaktischer Dokumentation

---

## 🚀 Quickstart

### 1. Repository klonen
```bash
git clone https://github.com/<user>/chroma-core
cd chroma-core
```

### 2. Virtuelle Umgebung erstellen
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. ChromaDB initialisieren
```bash
python3 -m src.setup.chroma_setup
```

### 5. Beispieldaten einfügen
```bash
python3 -m src.insert.insert_sample_data
```

### 6. Query ausführen (formatiert)
```bash
python3 -m src.query.query_pretty
```

---

## 📦 Projektstruktur

```
chroma-core/
│
├── docs/                     # Vollständige Dokumentation
├── data/                     # Daten für Features
├── src/                      # Setup-, Insert- und Query-Skripte
│   ├── setup/
│   ├── insert/
│   ├── query/
│   └── utils/
│
├── requirements.txt          # Reproduzierbare Abhängigkeiten
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧭 Wichtige Hinweise

### Python vs. Python3
- **In der venv:** `python` ist verfügbar
- **Außerhalb der venv:** Ubuntu nutzt `python3`

### Skripte immer als Modul ausführen
Damit Importe wie `from src.utils.pretty_print import pretty_print` funktionieren:

```bash
python3 -m src.query.query_pretty
```

**Nicht:**
```bash
python3 src/query/query_pretty.py
```

### GPU- und Telemetrie-Warnungen
ChromaDB nutzt ONNXRuntime.  
Wenn keine GPU vorhanden ist, erscheint:

```
GPU device discovery failed
```

Das ist **normal** und kein Fehler.

Telemetrie-Warnungen wie:

```
Failed to send telemetry event ...
```

sind ebenfalls harmlos.  
Sie können ignoriert oder später deaktiviert werden.

---

## 🧩 Wie man Features hinzufügt

Neue Features werden als Branch angelegt:

```bash
git checkout -b feature/<feature-name>
```

Struktur für Features:

```
data/<feature-name>/                 # Daten
src/insert/<feature-name>/           # Insert-Skripte
src/query/<feature-name>/            # Query-Skripte
docs/features/<feature-name>.md      # Dokumentation
```

---

## 📚 Dokumentation

Alle Schritte sind ausführlich beschrieben im Ordner:

```
docs/

Empfohlene Reihenfolge:

1. `00-intro.md`
2. `01-prerequisites.md`
3. `02-environment-setup.md`
4. `03-install-chromadb.md`
5. `04-create-collection.md`
6. `05-query-data.md`
7. `06-troubleshooting.md`
8. `07-how-to-add-features.md`

```

---

# 📘 ** How‑to‑Use **  

# How to Use Chroma Core

## 1. Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. ChromaDB starten
```bash
python3 -m src.setup.chroma_setup
```

## 3. Daten einfügen
```bash
python3 -m src.insert.insert_sample_data
```

## 4. Daten abfragen
Rohformat:
```bash
python3 -m src.query.query_raw
```

Formatiert:
```bash
python3 -m src.query.query_pretty
```

## 5. Feature hinzufügen
```bash
git checkout -b feature/<name>
```

Daten:
```
data/<name>/
```

Insert:
```
src/insert/<name>/
```

Query:
```
src/query/<name>/
```

Dokumentation:
```
docs/features/<name>.md
```