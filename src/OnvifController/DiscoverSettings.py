from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from onvif import ONVIFService

#from UI.MainWindow.MainWindow import MainWindow
from UI.DiscoverSettings.discoversettings_ui import Ui_Dialog

import re
 
def is_valid_IP(str):
    return bool(re.match(r'^((0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.|$)){4}$', str))

class DiscovererSettings(QDialog, Ui_Dialog):

    def __init__(self, disc,  mw, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.disc = disc
        self.applybutton.pressed.connect(self.apply)
        self.exitButton.pressed.connect(self.close)
        mw.actionDiscover_Settings.triggered.connect(self.mostrar)

    def apply(self):
        ip = self.bclineedit.text()
        if not is_valid_IP(ip):
            QMessageBox.critical(None, "Exception","Not a valid IP")
        else:
            self.disc.setdtip(self.timeoutbox.value(), ip) 
            self.close()

    def print_dades(self):
       self.bclineedit.setText(self.disc.bcip)
       self.timeoutbox.setValue(self.disc.discoverytime)

    def mostrar(self):
        self.print_dades()
        self.exec()