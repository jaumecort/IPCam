# This Python file uses the following encoding: utf-8
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.main_window.main_window_ui import Ui_MainWindow

from development.OnvifDiscovery.OnvifDiscoverer import OnvifDiscovery

class Camera:
    def __init__(self) -> None:
        self.status_connected = False
        pass

    def connect(self, ip):
        if not self.status_connected:
            print("Connected to "+ip)
            return True
        else: 
            print("Not connected")
            return False

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        # Treadings no se se fan falta
        self.threadpool = QThreadPool()
        print("Multithreading UI with maximum %d threads" % self.threadpool.maxThreadCount())
        
        # Aqui definirem els objectes necessaris:
        self.cam = Camera()


        #Aqui connectarem totes les senyals amb funcions propies
    def connectSignalsSlots(self):
        #self.actionDiscover.triggered.connect(self.connect)
        self.actionConnection.triggered.connect(self.connect)

        #cada funcio propia realitzara els canvis gui necessaris
    def connect(self):
        if self.cam.connect(self.ipLineEdit.text()):
            self.statusLabel.setText("Connected")
        else: 
            self.statusLabel.setText("Disconnected")




