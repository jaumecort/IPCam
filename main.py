import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.UI_Controller import UI_Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI_Controller()
    win.show()
    sys.exit(app.exec())
