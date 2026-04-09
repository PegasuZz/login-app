# Login-App – Dokumentation

> **Tipp:** Fülle jeden Abschnitt in deinen eigenen Worten aus.
> Das hilft dir, das Gelernte zu festigen und macht das Projekt für andere verständlich.

---

## Was macht dieses Projekt?

<!-- Beschreibe hier kurz was die App macht, welches Problem sie löst und wer sie benutzen würde. -->

---

## Technologien

| Technologie    | Verwendungszweck                                      |
|---------------|-------------------------------------------------------|
| Python / Flask | Web-Framework für Routen und Session-Handling         |
| SQLite         | Lokale Datenbank für Benutzer                         |
| flask-bcrypt   | Sicheres Hashen von Passwörtern                       |
| python-dotenv  | Laden von Umgebungsvariablen aus `.env`               |

---

## Installation

<!-- Schreibe hier die Schritte, die jemand braucht um die App bei sich zum Laufen zu bringen. -->
<!-- Beispiel: -->

```bash
# 1. Repository klonen
git clone https://github.com/DEIN-USERNAME/login-app.git
cd login-app

# 2. Virtual Environment erstellen und aktivieren
python -m venv venv
source venv/bin/activate  # macOS/Linux
# oder: venv\Scripts\activate  # Windows

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. .env Datei anlegen
echo "SECRET_KEY=dein-geheimer-schlüssel" > .env

# 5. App starten
python app.py
```

---

## Benutzung

<!-- Erkläre wie man die App benutzt. Welche Seiten gibt es? Wie loggt man sich ein? -->

| Route        | Beschreibung                                  |
|-------------|-----------------------------------------------|
| `/`          | Login-Seite                                   |
| `/register`  | Neuen Account erstellen                        |
| `/dashboard` | Nur zugänglich nach erfolgreichem Login        |
| `/logout`    | Session beenden, zurück zur Login-Seite        |

---

## Code-Struktur

<!-- Erkläre in deinen eigenen Worten was jede Datei macht. -->

```
login-app/
├── app.py          # ...
├── database.py     # ...
├── templates/
│   ├── login.html      # ...
│   ├── register.html   # ...
│   └── dashboard.html  # ...
├── .env            # ...
├── .gitignore      # ...
└── requirements.txt # ...
```

---

## Sicherheit – Was habe ich beachtet?

<!-- Erkläre warum Passwörter gehasht werden, was bcrypt ist, warum .env nicht ins Git kommt, usw. -->

---

## Git Workflow

<!-- Beschreibe die Git-Befehle die du benutzt hast und was sie bedeuten. -->

```bash
# Repository klonen
git clone ...

# Änderungen hochladen
git add .
git commit -m "Meine Änderung"
git push origin main

# Neueste Version holen
git pull origin main
```

---

## Was habe ich dabei gelernt?

<!-- Das ist der wichtigste Abschnitt! Schreibe auf was neu für dich war, was überraschend war, und was du beim nächsten Mal anders machen würdest. -->

---

## Bekannte Einschränkungen / Mögliche Erweiterungen

<!-- Was könnte man noch verbessern? Z.B. Passwort zurücksetzen, E-Mail-Bestätigung, etc. -->
