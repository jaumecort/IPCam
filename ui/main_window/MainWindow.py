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
        self.vf = VideoFeeder(self)
        self.cam = Camera(self.vf)
        
        self.consolecontroller=ConsoleController(self.console)
        self.connecter=Connecter(self.ipLineEdit, self.statusLabel, self.cam, self.consolecontroller, self.connectButton)
        
        #Setup ui i signals
        self.connectSignalsSlots()
        

        #Aqui connectarem totes les senyals amb funcions propies
    def connectSignalsSlots(self):
        self.actionDiscover.triggered.connect(self.connecter.discover)
        self.actionConnection.triggered.connect(self.connecter.buttonPressed)
        self.vf.changePixmap.connect(self.setImage)
        self.connecter.discoverer.discoveries.connect(self.connecter.printDiscoveries)

    
    
        




