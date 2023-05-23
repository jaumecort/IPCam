import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.MainWindow import MainWindow

if __name__ == "__main__":
    # Inicialitzam Applicació
    app = QApplication(sys.argv)

    # Inicialitzam Controlador IU
    win = MainWindow()
    win.show()

    sys.exit(app.exec())
