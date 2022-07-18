import mainWindow
import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QPalette, QColor


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle(QStyleFactory.create("Fusion"))

    # Style from https://gist.github.com/QuantumCD/6245215

    darkPalette = QPalette()
    darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    darkPalette.setColor(QPalette.Base, QColor(25, 25, 25))
    darkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    darkPalette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    darkPalette.setColor(QPalette.Text, QColor(255, 255, 255))
    darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    darkPalette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

    app.setPalette(darkPalette)

    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = mainWindow.CipherWindow(app)
    window.show()
    sys.exit(app.exec())
