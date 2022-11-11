from client.Window.window import MainWindow
from PySide6.QtWidgets import QApplication

import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())