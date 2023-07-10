from PyQt6.QtCore import QObject
from OnvifController.OnvifDiscoverer import OnvifDiscovery

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


from UI.MainWindow.workers.FeedBox import *
from UI.MainWindow.workers.PTZBox import *
from UI.MainWindow.workers.ConsoleBox import *

from OnvifController.CameraClient import CameraClient
from OnvifController.DiscoverSettings import DiscovererSettings
import json


class CameraBox:
    status_connected=False
    def __init__(self, mainwindow) -> None:

        ## Init de tots als accessos a MainWindow
        self.ipLineEdit:QLineEdit=mainwindow.ipLineEdit
        self.statusLabel:QLabel=mainwindow.statusLabel
        self.button=mainwindow.connectButton
        self.feedBox:FeedBox=mainwindow.feedBox
        self.discoverButton=mainwindow.discoverButton
        self.ptzBox:PTZBox=mainwindow.ptzBox

        self.disconectsignal = mainwindow.disconnectionSignal
        
        self.statusLabel.setText("Disconnected")
        self.statusLabel.setStyleSheet('color: red')
        self.ipLineEdit.setText(DiscovererSettings.data["ip"])

        ##Init dels objectes necessaris
        self.discoverer=Discoverer( self.ipLineEdit)
        self.connecter=Connecter(self.statusLabel, self.button, self.ipLineEdit, self.discoverButton, mainwindow.connectionSignal, self.status_connected)
        self.cameraClient = None

        ## Init de les senyals necessaries
        mainwindow.actionDiscover.triggered.connect(self.discover)
        mainwindow.actionConnection.triggered.connect(self.connect)
        self.discoverer.discoveries.connect(self.printDiscoveries)
    
        pass

    # Quan s'apreta el botó de connect:
    def connect(self):  
        if self.status_connected:
            self.cameraClient = None
            self.status_connected=False
            self.layout_disconnect()
            self.disconectsignal.emit()
        else:
            self.discoverButton.setEnabled(False)
            self.statusLabel.setText("Connecting...")
            self.statusLabel.setStyleSheet('color: orange')
            if self.ipLineEdit.text() != '0':
                cred = SimpleLogin.logindata()
            else:
                cred = None
            self.connecter.setCredentials(cred)
            self.connecter.start()

    def layout_disconnect(self):
        self.statusLabel.setText("Disconnected")
        self.statusLabel.setStyleSheet('color: red')
        self.button.setText("Connect")
        self.ipLineEdit.setEnabled(True)
        self.discoverButton.setEnabled(True)
            

        
    # Quan s'apreta el botó de Discover
    def discover(self):
        self.discoverButton.setEnabled(False)
        self.button.setEnabled(False)
        self.ipLineEdit.setEnabled(False)
        self.discoverer.start()

    def printDiscoveries(self, devs:dict):
        ips = devs.keys()
        self.discoverButton.setEnabled(True)
        self.button.setEnabled(True)
        self.ipLineEdit.setEnabled(True)
        if not ips:
            ConsoleBox.afegirMissatge("No devices found")
            pass
        for ip in ips:
            ConsoleBox.afegirMissatge("Device found: ["+ip+"]")
            self.ipLineEdit.setText(ip)



class Discoverer(QThread):
    discoveries=pyqtSignal(dict)
    def __init__(self, ipline) -> None:
        super().__init__()
        self.ipline = ipline
        pass

    # Quan s'apreta el botó de Discover
    def run(self):
        DiscovererSettings.read_json()
        self.discoverytime = DiscovererSettings.data["Discovery time"]
        self.bcip = DiscovererSettings.data["Broadcast IP"]
        ConsoleBox.afegirMissatge("Discovering devices: Broadcast IP: "+self.bcip+" Timeout: "+str(self.discoverytime)+" seconds")
        devs= OnvifDiscovery(self.bcip, self.discoverytime)
        self.discoveries.emit(devs)

from UI.SimpleLogin.SimpleLogin import *
class Connecter(QThread):
    cred = {}
    def setCredentials(self, creds):
        self.cred = creds

    def __init__(self, statusLabel, button, ipLineEdit, dbut, consignal, status) -> None:
        super().__init__()
        self.statusLabel = statusLabel
        self.button = button
        self.ipLineEdit = ipLineEdit
        self.discoverButton = dbut
        self.connection=consignal
        self.status_connected = status
        pass

    def run(self):
        try:
            self.ipLineEdit.setEnabled(False)
            self.button.setEnabled(False)
            self.cameraClient = CameraClient(self.ipLineEdit.text(), self.cred)
            self.connection.emit(self.cameraClient)
            self.statusLabel.setText("Connected")
            self.statusLabel.setStyleSheet('color: green')
            ConsoleBox.afegirMissatge("Connection stablished ["+self.ipLineEdit.text()+"]")
            self.button.setText("Disconnect")
            self.button.setEnabled(True)
            DiscovererSettings.data['ip']=self.ipLineEdit.text()
            DiscovererSettings.write_json()
        except:
            ConsoleBox.afegirMissatge("Connection Failed! ["+self.ipLineEdit.text()+"]")
            self.statusLabel.setText("Disconnected")
            self.statusLabel.setStyleSheet('color: red')
            self.ipLineEdit.setEnabled(True)
            self.button.setEnabled(True)
            self.discoverButton.setEnabled(True)
           
