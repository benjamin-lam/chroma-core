# Virtuelle Umgebung einrichten

venv anlegen
```bash
python3 -m venv .venv
```

Aktivieren
```bash
source .venv/bin/activate
```

Prüfen, ob die venv aktiv ist
```bash
which python
python --version
```


## 🔍 Warum virtuelle Umgebungen? (Und warum aktivieren?)

Vielleicht hast du schon einmal `pip install chromadb` ausprobiert und es hat funktioniert – wozu also der Umweg über `venv`?  
Und warum muss ich die Umgebung jedes Mal **aktivieren**, bevor ich mein Skript starte?

Dieser Abschnitt erklärt genau das – **einfach und ohne Fachchinesisch**.

---

### 📦 1. Was ist eine virtuelle Umgebung?

Stell dir vor, du arbeitest an mehreren Python-Projekten:

- Projekt A benötigt **ChromaDB 0.5.4**
- Projekt B benötigt **ChromaDB 0.6.0** (weil es eine neue Funktion nutzt)

Wenn du beide Pakete **global** auf deinem Rechner installierst, überschreiben sie sich gegenseitig.  
Im schlimmsten Fall funktioniert plötzlich keines der Projekte mehr.

**Eine virtuelle Umgebung ist ein eigener, abgeschotteter Ordner (`.venv/`), der genau die Pakete enthält, die *dieses eine Projekt* braucht.**  
Andere Projekte haben ihre eigenen Umgebungen – Konflikte sind unmöglich.

> ✅ **Vorteile auf einen Blick**
> - Kein Chaos bei verschiedenen Paketversionen
> - Keine Administratorrechte nötig (alles im Projektordner)
> - Reproduzierbar: Jeder, der dein Projekt klont, bekommt genau die gleichen Abhängigkeiten

---

### 🔌 2. Warum muss ich die Umgebung **aktivieren**?

Eine virtuelle Umgebung ist zunächst nur ein **Ordner**.  
Damit Python und pip wissen, dass sie **diesen Ordner** und nicht das System benutzen sollen, musst du die Umgebung **aktivieren**.

**Was passiert beim Aktivieren?**

- Dein `PATH` wird geändert: `python` und `pip` zeigen jetzt auf die Version **innerhalb** von `.venv/`.
- Die Umgebungsvariable `VIRTUAL_ENV` wird gesetzt.
- (Oft) ändert sich dein Terminal‑Prompt – du siehst `(.venv)` vor der Eingabezeile.

**Ohne Aktivierung** passiert Folgendes:

```bash
python myscript.py   # ruft das System‑Python auf (global)
```

Dort ist ChromaDB **nicht installiert** – also erscheint:

```
ModuleNotFoundError: No module named 'chromadb'
```

Genau dieser Fehler ist das sicherste Zeichen: **Du hast vergessen, die virtuelle Umgebung zu aktivieren.**

> ⚠️ **Merke:**  
> `pip install -r requirements.txt` und `python src/...` müssen **immer** mit aktivierter Umgebung ausgeführt werden.  
> Einmal aktiviert, bleibt sie für das gesamte Terminalfenster gültig.

---

### ✅ 3. Woran erkenne ich, dass die Umgebung aktiv ist?

| Methode | Wenn aktiviert | Wenn nicht aktiviert |
|--------|----------------|----------------------|
| **Terminal‑Prompt** | `(.venv) user@pc:~$` | `user@pc:~$` |
| `which python` | `/dein/pfad/.venv/bin/python` | `/usr/bin/python` (oder ähnlich) |
| `echo $VIRTUAL_ENV` | `/dein/pfad/.venv` | (leer) |
| `pip list` | Nur die Pakete aus `.venv/` | Globale Pakete |

---

### 🧪 4. Kurzer Test für dein Setup

Nachdem du `.venv` erstellt und **aktiviert** hast:

```bash
pip install -r requirements.txt
python -c "import chromadb; print(chromadb.__version__)"
```

Kein Fehler? → Perfekt! Du bist startklar.

Falls doch `ModuleNotFoundError` erscheint:  
→ Bist du **sicher**, dass das venv aktiv ist?  
→ Manchmal hilft es, das venv neu anzulegen und dann *sofort* zu aktivieren.

---

### 💡 5. (Optional) Muss ich *immer* manuell aktivieren?

Ja – aber es gibt Helfer:

- **VS Code** erkennt `.venv/` oft automatisch und aktiviert es beim Öffnen des Terminals.
- **direnv / autoenv** können das Aktivieren beim Betreten des Projektordners übernehmen.

Für den Anfang ist die manuelle Aktivierung aber völlig ausreichend und hilft dir zu verstehen, was im Hintergrund passiert.

---

**Zusammengefasst:**  
Virtuelle Umgebungen sind die **Hausapotheke** für Python‑Projekte – sie verhindern Kopfschmerzen bei Paketkonflikten.  
Die Aktivierung ist der **Schlüssel**, der diese Apotheke erst öffnet. Ohne Schlüssel: kein Zugriff auf ChromaDB.

---

*Wenn du noch mehr Hintergrund lesen möchtest: [Python Packaging Authority – Virtual Environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)*