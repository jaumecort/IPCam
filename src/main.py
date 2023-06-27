import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from UI.MainWindow import MainWindow

from UI.SimpleLogin.SimpleLogin import *

if __name__ == "__main__":
    # Inicialitzam Applicació
    app = QApplication(sys.argv)

    # Inicialitzam Controlador IU
    win = MainWindow.MainWindow()
    win.show()  

    sys.exit(app.exec())
