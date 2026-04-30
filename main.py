import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class CompilerMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.setWindowTitle("Compiler UI - PySide6")
        self.setGeometry(100, 100, 800, 600) # x, y, width, height

        # Add a temporary placeholder label
        self.label = QLabel("Welcome to the Compiler Development Environment", self)
        self.label.setGeometry(200, 250, 400, 50)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Instantiate and show the main window
    window = CompilerMainWindow()
    window.show()

    # Run the application event loop
    sys.exit(app.exec())
