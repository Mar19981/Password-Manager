import mainWindow, sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainWindow.CipherWindow(app)
    window.show()
    sys.exit(app.exec())