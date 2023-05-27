# This Python file uses the following encoding: utf-8
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.main_window.main_window_ui import Ui_MainWindow


from ui.main_window.workers.VideoFeed import *
from ui.main_window.workers.CameraBox import *
from ui.main_window.workers.Console import *



class MainWindow(QMainWindow, Ui_MainWindow):

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.labelVideo.setPixmap(QPixmap.fromImage(image))

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        #vf.start()
        # Aqui definirem els objectes necessaris:
        
        self.cam = Camera()
        
        self.consolecontroller=ConsoleController(self.console)
        self.connecter=CameraBox(self.ipLineEdit, self.statusLabel, self.cam, self.consolecontroller, self.connectButton)
        
        #Setup ui i signals
        self.connectSignalsSlots()
        

        #Aqui connectarem totes les senyals amb funcions propies
    def connectSignalsSlots(self):
        #Boto discover
        self.actionDiscover.triggered.connect(self.connecter.discover)
        #Boto connect
        self.actionConnection.triggered.connect(self.connecter.buttonPressed)
        #Senyal per canviar la imatge
        self.cam.vf.changePixmap.connect(self.setImage)
        self.connecter.discoverer.discoveries.connect(self.connecter.printDiscoveries)

    
    
        




