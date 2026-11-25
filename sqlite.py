import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

# Datenbank öffnen
db = sqlite3.connect("test.db")

db.execute("""
    CREATE TABLE IF NOT EXISTS clicks (
        id INTEGER PRIMARY KEY,
        text TEXT
    )
""")
db.commit()


def speichern():
    db.execute("INSERT INTO clicks (text) VALUES (?)", ("Klick",))
    db.commit()
    print("Gespeichert!")


app = QApplication(sys.argv)

window = QWidget()
window.resize(800, 600)

button = QPushButton("Speichern", window)
button.move(20, 20)
button.clicked.connect(speichern)

window.show()
app.exec()

db.close()
