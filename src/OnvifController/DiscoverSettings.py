from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from onvif import ONVIFService

#from UI.MainWindow.MainWindow import MainWindow
from UI.DiscoverSettings.discoversettings_ui import Ui_Dialog
from UI.MainWindow.workers.ConsoleBox import ConsoleBox
import re, json
 
def is_valid_IP(str):
    return bool(re.match(r'^((0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.|$)){4}$', str))

class DiscovererSettings(QDialog, Ui_Dialog):
    data = None
    def __init__(self, mw, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.applybutton.pressed.connect(self.apply)
        self.exitButton.pressed.connect(self.close)
        mw.actionDiscover_Settings.triggered.connect(self.mostrar)   
        DiscovererSettings.read_json()
          
    def print_dades(self):
        self.bclineedit.setText(self.data['Broadcast IP'])
        self.timeoutbox.setValue(self.data['Discovery time'])
        

    def mostrar(self):
        DiscovererSettings.read_json()
        self.print_dades()
        self.exec()

    def apply(self):
        self.data['Broadcast IP'] = self.bclineedit.text()
        self.data['Discovery time'] = self.timeoutbox.value()
        if not is_valid_IP(self.data['Broadcast IP']):
            QMessageBox.critical(None, "Exception","Not a valid IP")
        else:
            DiscovererSettings.write_json()
            self.close() 

    def read_json():
        try:
            with open('config\connection_settings.json', 'r') as f:
                DiscovererSettings.data = json.load(f)
        except Exception as e:
            ConsoleBox.afegirMissatge(str(e)) 
        return DiscovererSettings.data

    def write_json():
        try:
            with open('config\connection_settings.json', 'w') as f:
                f.write(json.dumps(DiscovererSettings.data, indent=2))
        except Exception as e:
            ConsoleBox.afegirMissatge(str(e)) 