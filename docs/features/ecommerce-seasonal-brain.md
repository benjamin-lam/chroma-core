# E‑Commerce Seasonal Brain (POC)

Dieses Feature beantwortet eine der wichtigsten Fragen im E‑Commerce:

> „WTF sollte ich heute tun, damit mein Shop erfolgreich bleibt –  
> und ich nicht plötzlich im Weihnachtsstress lande?“

Dieses Modul ist ein **Proof of Concept (POC)**.  
Es zeigt, wie man saisonale Ereignisse (Valentinstag, Ostern, Black Friday, Weihnachten)  
mit Lead‑Times, To‑Dos und Checklisten in einer ChromaDB speichern und abfragen kann.

Es ist **nicht** als vollständiges Produktionssystem gedacht, sondern als:

- Demonstration einer strukturierten Wissensbasis  
- Beispiel für semantische Abfragen  
- Grundlage für Agenten‑Workflows  
- Inspiration für echte E‑Commerce‑Automatisierung  

---

## 🧠 Warum dieses Feature wichtig ist

Ein echter E‑Commerce‑Manager arbeitet **nicht** so:

- „Ich mache nur etwas, wenn es exakt 8 Wochen vorher ist.“

Sondern eher so:

- „Was ist als nächstes fällig?“  
- „Was ist überfällig?“  
- „Was sollte ich diese Woche tun?“  
- „Was sollte ich diesen Monat tun?“  

Genau deshalb enthält dieses Feature **drei zusätzliche Query‑Skripte**,  
die realistischere Workflows abbilden.

---

## 📦 Enthaltene Daten

Die Datei:

```
data/ecommerce-seasonal-brain/events.json
```

enthält:

- Saisonale Events (Valentinstag, Ostern, Black Friday, Weihnachten)
- Exakte Event‑Daten
- Lead‑Times (z. B. 8 Wochen vorher: Sortiment planen)
- Marketing‑Checklisten
- Logistik‑Checklisten
- Operations‑Checklisten

Diese Daten sind **Beispieldaten** und dienen als POC‑Grundlage.

---

## 🧰 Insert‑Skript

Daten in ChromaDB einfügen:

```bash
python3 -m src.insert.ecommerce-seasonal-brain.insert_events
```

---

## 🔍 Query‑Skripte

### 1. **Nächstes Event**
```bash
python3 -m src.query.ecommerce-seasonal-brain.next_event
```
Zeigt das nächste saisonale Ereignis und die verbleibenden Tage.

---

### 2. **Was steht als nächstes an?**
```bash
python3 -m src.query.ecommerce-seasonal-brain.next_upcoming_todos
```
Findet das **nächste fällige To‑Do**, basierend auf Lead‑Times.

---

### 3. **Was muss ich diese Woche tun?**
```bash
python3 -m src.query.ecommerce-seasonal-brain.todos_this_week
```
Zeigt alle Aufgaben, die **innerhalb der nächsten 7 Tage** fällig sind.

---

### 4. **Was habe ich verpasst?**
```bash
python3 -m src.query.ecommerce-seasonal-brain.overdue_todos
```
Listet alle Aufgaben auf, deren Lead‑Time **bereits in der Vergangenheit** liegt.

---

## ⚠️ Limitierungen (POC)

Dieses Feature ist bewusst einfach gehalten:

- Lead‑Times sind statisch (z. B. „8 Wochen vorher“)
- Es gibt keine Priorisierung nach Umsatzpotenzial
- Es gibt keine Produkt‑ oder Kategorie‑Daten
- Es gibt keine dynamischen Forecasts
- Es gibt keine Integration mit Shop‑Systemen
- Es gibt keine automatische Benachrichtigung

Der Fokus liegt auf:

- Datenstruktur
- Query‑Logik
- Erweiterbarkeit
- Verständlichkeit

---

## 🚀 Erweiterungsideen

Dieses POC kann leicht erweitert werden:

- Monats‑Ansicht („Was sollte ich im März tun?“)
- Umsatz‑basierte Priorisierung
- Integration mit Shopify, Shopware, WooCommerce
- Automatische Tages‑Benachrichtigungen
- Agenten‑Workflows („Erstelle Kampagnen für das nächste Event“)
- Dashboard (Next.js)
- API (FastAPI)
- KI‑gestützte Forecasts

---

## 📌 Fazit

Dieses Feature zeigt, wie man saisonale E‑Commerce‑Planung  
in eine strukturierte Wissensbasis überführt.

Es ist ein **POC**, kein fertiges Produkt –  
aber eine hervorragende Grundlage für echte Automatisierung.