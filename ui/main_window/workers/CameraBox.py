from development.OnvifDiscovery.OnvifDiscoverer import OnvifDiscovery

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.main_window.workers.FeedBox import *
from ui.main_window.workers.ConsoleBox import *
import ui.main_window.MainWindow as mw

from development.CameraClient.CameraClient import CameraClient


class CameraBox:
    status_connected=False
    def __init__(self, mainwindow) -> None:
        ## Init de tots als accessos a MainWindow
        self.ipLineEdit=mainwindow.ipLineEdit
        self.statusLabel=mainwindow.statusLabel
        self.console:ConsoleBox=mainwindow.consoleBox
        self.button=mainwindow.connectButton
        self.feedBox:FeedBox=mainwindow.feedBox
        

        ##Init dels objectes necessaris
        self.discoverer=Discoverer(self.console, self.ipLineEdit)
        self.cameraClient = None

        ## Init de les senyals necessaries
        mainwindow.actionDiscover.triggered.connect(self.discover)
        self.discoverer.discoveries.connect(self.printDiscoveries)
        pass

    # Quan s'apreta el botó de connect:
    def connect(self):
        print("Implementar conex/desconex")
        if self.status_connected:
            self.cameraClient = None
            self.statusLabel.setText("Disconnected")
            self.button.setText("Connect")
            self.status_connected=False
            self.feedBox.stopFeed()
            
        else:
            self.cameraClient = CameraClient(self.ipLineEdit.text())
            self.statusLabel.setText("Connected")
            self.console.afegirMissatge("Connectat correctament a "+self.ipLineEdit.text())
            self.button.setText("Disconnect")
            self.status_connected=True
            self.feedBox.startFeed(self.cameraClient.getStreamUri())
    
    # Quan s'apreta el botó de Discover
    def discover(self):
        self.console.afegirMissatge("Cercant Cameres a la xarxa...")
        self.discoverer.start()

    def printDiscoveries(self, devs:dict):
        ips = devs.keys()
        if not ips:
            self.console.afegirMissatge("No sha trobat res")
            pass
        for ip in ips:
            self.console.afegirMissatge("Sha trobat camara amb ip "+ip+" i URI: "+devs[ip])
            self.ipLineEdit.setText(ip)



class Discoverer(QThread):
    discoveries=pyqtSignal(dict)

    def __init__(self, console, ipline) -> None:
        super().__init__()
        self.console = console
        self.ipline = ipline
        pass

    # Quan s'apreta el botó de Discover
    def run(self):
        devs= OnvifDiscovery("255.255.255.255")
        self.discoveries.emit(devs)
           