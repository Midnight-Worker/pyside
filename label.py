import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel
)

app = QApplication(sys.argv)

window = QWidget()
window.resize(800, 600)

layout = QVBoxLayout(window)

label = QLabel("Hallo Welt")
button = QPushButton("Klick mich")

layout.addWidget(label)
layout.addWidget(button)
layout.addStretch()

button.clicked.connect(lambda: label.setText("Geklickt!"))

window.show()
sys.exit(app.exec())
