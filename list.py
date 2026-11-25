import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QListWidget, QVBoxLayout
)

db = sqlite3.connect("test.db")
db.execute("""
    CREATE TABLE IF NOT EXISTS clicks (
        id INTEGER PRIMARY KEY,
        text TEXT
    )
""")
db.commit()


def laden():
    liste.clear()

    for row in db.execute("SELECT * FROM clicks"):
        liste.addItem(f"{row[0]}: {row[1]}")


def speichern():
    db.execute("INSERT INTO clicks (text) VALUES (?)", ("Klick",))
    db.commit()
    laden()


app = QApplication(sys.argv)

window = QWidget()
window.resize(800, 600)

layout = QVBoxLayout(window)

button = QPushButton("Speichern")
liste = QListWidget()

layout.addWidget(button)
layout.addWidget(liste)

button.clicked.connect(speichern)

laden()
window.show()
app.exec()

db.close()
