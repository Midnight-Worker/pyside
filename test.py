import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.resize(800, 600)

button = QPushButton("Klick mich", window)
button.move(20, 20)

window.show()
sys.exit(app.exec())
