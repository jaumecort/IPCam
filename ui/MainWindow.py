# This Python file uses the following encoding: utf-8
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.main_window.main_window_ui import Ui_MainWindow

from development import *

from development.OnvifDiscovery.OnvifDiscoverer import OnvifDiscovery

class Connecter:
    def __init__(self, ipline, label, cam, console) -> None:
        self.ipLineEdit=ipline
        self.statusLabel=label
        self.cam=cam
        self.console=console
        pass

    def connect(self):
        if self.cam.connect(self.ipLineEdit.text()):
            self.statusLabel.setText("Connected")
            self.console.afegirMissatge("Connectat correctament a "+self.ipLineEdit.text())
        else: 
            self.statusLabel.setText("Disconnected")
            self.console.afegirMissatge("No sha pogut connectar correctament a "+self.ipLineEdit.text())

class Discoverer:
    def __init__(self, console, ipline) -> None:
        self.console = console
        self.ipline = ipline
        pass

    def discover(self):
        ips, uri = OnvifDiscovery("255.255.255.255")
        if not ips:
            self.console.afegirMissatge("No sha trobat res")
            pass
        for ip in ips:
            self.console.afegirMissatge("Sha trobat camara amb ip "+ip)
            self.ipline.setText(ip)

class ConsoleController:
    def __init__(self, console) -> None:
        self.console = console
        pass

    def afegirMissatge(self, missatge):
        self.console.append(missatge)

class Camera:
    def __init__(self) -> None:
        self.status_connected = False
        pass

    def connect(self, ip):
        if not self.status_connected:
            print("Connected to "+ip)
            self.status_connected = True
            return True
        else: 
            print("Not connected")
            self.status_connected = False
            return False

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Aqui definirem els objectes necessaris:
        self.cam = Camera()
        self.consolecontroller=ConsoleController(self.console)
        self.discoverer=Discoverer(self.consolecontroller, self.ipLineEdit)
        self.connecter=Connecter(self.ipLineEdit, self.statusLabel, self.cam, self.consolecontroller)

        #Setup ui i signals
        self.connectSignalsSlots()

        # Treadings no se se fan falta
        self.threadpool = QThreadPool()
        print("Multithreading UI with maximum %d threads" % self.threadpool.maxThreadCount())
        

        #Aqui connectarem totes les senyals amb funcions propies
    def connectSignalsSlots(self):
        self.actionDiscover.triggered.connect(self.discoverer.discover)
        self.actionConnection.triggered.connect(self.connecter.connect)

        #cada funcio propia realitzara els canvis gui necessaris
    
      
        




