import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meine Anwendung")
        self.resize(800, 600)

        # Zentrales Widget
        central = QWidget()
        self.setCentralWidget(central)

        # Layout
        layout = QVBoxLayout(central)

        # Widgets
        self.label = QLabel("Hallo Welt!")
        self.input = QLineEdit()
        self.button = QPushButton("Klick mich")

        # Widgets zum Layout hinzufügen
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addStretch()

        # Events
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.label.setText(self.input.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
