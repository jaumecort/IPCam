import typing
from PyQt6.QtCore import QObject
from OnvifDiscovery.OnvifDiscoverer import OnvifDiscovery

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


from UI.MainWindow.workers.FeedBox import *
from UI.MainWindow.workers.PTZBox import *
from UI.MainWindow.workers.ConsoleBox import *
import UI.MainWindow.MainWindow as mw

from CameraClient.CameraClient import CameraClient


class CameraBox:
    status_connected=False
    def __init__(self, mainwindow) -> None:
        ## Init de tots als accessos a MainWindow
        self.ipLineEdit:QLineEdit=mainwindow.ipLineEdit
        self.statusLabel=mainwindow.statusLabel
        self.console:ConsoleBox=mainwindow.consoleBox
        self.button=mainwindow.connectButton
        self.feedBox:FeedBox=mainwindow.feedBox
        self.discoverButton=mainwindow.discoverButton
        self.ptzBox:PTZBox=mainwindow.ptzBox
        

        ##Init dels objectes necessaris
        self.discoverer=Discoverer(self.console, self.ipLineEdit)
        self.connecter=Connecter(self.statusLabel, self.button, self.ipLineEdit, self.console, self.discoverButton)
        self.cameraClient = None

        ## Init de les senyals necessaries
        mainwindow.actionDiscover.triggered.connect(self.discover)
        self.discoverer.discoveries.connect(self.printDiscoveries)
        self.connecter.connection.connect(self.setConnection)
        pass

    # Quan s'apreta el botó de connect:
    def connect(self):  
        if self.status_connected:
            self.cameraClient = None
            self.statusLabel.setText("Disconnected")
            self.button.setText("Connect")
            self.status_connected=False
            self.ipLineEdit.setEnabled(True)
            self.feedBox.stopFeed()
            self.discoverButton.setEnabled(True)
            
        else:
           self.discoverButton.setEnabled(False)
           self.connecter.start()
            
    def setConnection(self, client:CameraClient):
        self.cameraClient = client     
        self.status_connected=True  
        self.statusLabel.setText("Connected")
        self.console.afegirMissatge("Connection stablished ["+self.ipLineEdit.text()+"]")
        self.button.setText("Disconnect")
        self.button.setEnabled(True)
        self.feedBox.startFeed(self.cameraClient.getStreamUri())
        self.ptzBox.connectPTZ(self.cameraClient.mycam)
        
        
           
    
    # Quan s'apreta el botó de Discover
    def discover(self):
        self.discoverButton.setEnabled(False)
        self.button.setEnabled(False)
        self.ipLineEdit.setEnabled(False)
        self.console.afegirMissatge("Discovering devices")
        self.discoverer.start()

    def printDiscoveries(self, devs:dict):
        ips = devs.keys()
        self.discoverButton.setEnabled(True)
        self.button.setEnabled(True)
        self.ipLineEdit.setEnabled(True)
        if not ips:
            self.console.afegirMissatge("No devices found")
            pass
        for ip in ips:
            self.console.afegirMissatge("Device found: ["+ip+"]")
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

class Connecter(QThread):
    connection=pyqtSignal(CameraClient)

    def __init__(self, statusLabel, button, ipLineEdit, console, dbut) -> None:
        super().__init__()
        self.statusLabel = statusLabel
        self.button = button
        self.ipLineEdit = ipLineEdit
        self.console = console
        self.discoverButton = dbut
        pass

    def run(self):
        try:
            self.ipLineEdit.setEnabled(False)
            self.button.setEnabled(False)
            self.cameraClient = CameraClient(self.ipLineEdit.text())
            self.connection.emit(self.cameraClient)
        except:
            self.console.afegirMissatge("Connection Failed! ["+self.ipLineEdit.text()+"]")
            self.ipLineEdit.setEnabled(True)
            self.button.setEnabled(True)
            self.discoverButton.setEnabled(True)
           