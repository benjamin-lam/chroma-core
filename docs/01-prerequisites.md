# Vorbedingungen prüfen

## Python-Version prüfen

```bash
python3 --version
```

Erwartete Ausgabe (Beispiel):
```bash
Python 3.12.x
```

Falls kein Python installiert ist:
```bash
sudo apt update
sudo apt install python3
```

## Prüfen, ob pip installiert ist

```bash
pip3 --version
```
Falls pip fehlt:
```bash
sudo apt install python3-pip
```

### Prüfen, ob das venv‑Modul installiert ist

```bash
python3 -m venv testenv
```

Wenn du folgende Fehlermeldung bekommst:
```bash
The virtual environment was not created successfully because ensurepip is not available.
```

→ Dann fehlt das Paket python3.12-venv (oder die passende Version).

Installieren:
```bash
sudo apt install python3.12-venv
```
