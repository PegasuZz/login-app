import sqlite3
import os
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Erstellt die Datenbank und die users-Tabelle, falls noch nicht vorhanden."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        conn.commit()


def create_user(username: str, password: str) -> bool:
    """
    Legt einen neuen User an. Passwort wird gehasht gespeichert.
    Gibt True zurück bei Erfolg, False wenn Username bereits existiert.
    """
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def get_user(username: str):
    """Gibt den User als Row-Objekt zurück, oder None wenn nicht gefunden."""
    with get_connection() as conn:
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
    return user


def verify_password(plain_password: str, password_hash: str) -> bool:
    """Prüft ob das eingegebene Passwort zum gespeicherten Hash passt."""
    return bcrypt.check_password_hash(password_hash, plain_password)


if __name__ == "__main__":
    # Direkt ausführen um DB zu initialisieren und einen Test-User anzulegen
    init_db()
    print("Datenbank initialisiert.")

    success = create_user("admin", "geheimes_passwort")
    if success:
        print("Test-User 'admin' wurde angelegt.")
    else:
        print("User 'admin' existiert bereits.")
