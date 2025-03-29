# Discord Scheduled Message Bot

Dieser Bot sendet automatisch geplante Nachrichten mit Bildern in einem Discord-Kanal. Jede Nachricht kann individuell eine Löschzeit haben.

## Voraussetzungen

- Python 3.8 oder höher
- `discord.py`
- `apscheduler`

### Installation

1. Klone das Repository oder speichere die Skriptdatei.
2. Installiere die benötigten Abhängigkeiten mit:
   ```sh
   pip install discord.py apscheduler
   ```
3. Ersetze `YOUR_BOT_TOKEN` mit deinem Discord-Bot-Token.
4. Setze `CHANNEL_ID` auf die ID des Discord-Kanals, in den der Bot Nachrichten senden soll.
5. Stelle sicher, dass sich die Bilder (`bild1.jpg`, `bild2.jpg`, etc.) im selben Ordner wie das Skript befinden.

### Verwendung

- Der Bot sendet Nachrichten zu festgelegten Zeiten, die in der `scheduled_messages`-Liste definiert sind.
- Jede Nachricht kann:
  - Einen Titel und eine Beschreibung haben.
  - Ein Bild enthalten.
  - Eine eigene Löschzeit (`delete_after` in Sekunden) haben.

### Beispiel einer geplanten Nachricht

```python
scheduled_messages = [
    {
        "time": (0, 12, 0),  # Montag um 12:00 Uhr
        "messages": [
            {"title": "Erste Nachricht", "description": "Dies ist eine geplante Nachricht!", "image": "bild1.jpg", "delete_after": 60}
        ]
    }
]
```

### Starten des Bots

Führe den Bot mit folgendem Befehl aus:
```sh
python bot.py
```

### Lizenz
Dieses Projekt steht unter der MIT-Lizenz.
