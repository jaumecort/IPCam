from development.OnvifDiscovery.OnvifDiscoverer import OnvifDiscovery

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.main_window.workers.VideoFeed import *

class Camera:
    vf = VideoFeeder()
    def __init__(self) -> None:
        
        pass

    def disconnect(self):
        print("Implementar desconexió!")

        self.vf.setFeeding(False)
        return 


    def connect(self, ip):
        print("Implementar conexió!")
        self.status_connected = True
        self.vf.setFeeding(True)
        self.vf.start()
        return True

class CameraBox:
    status_connected=False
    def __init__(self, ipline, label, cam: Camera, console, button) -> None:
        self.ipLineEdit=ipline
        self.statusLabel=label
        self.cam=cam
        self.console=console
        self.button=button
        self.discoverer=Discoverer(self.console, self.ipLineEdit)
        pass

    # Quan s'apreta el botó de connect:
    def buttonPressed(self):
        if self.status_connected:
            self.cam.disconnect()
            self.statusLabel.setText("Disconnected")
            self.button.setText("Connect")
            self.status_connected=False
        else:
            self.cam.connect(self.ipLineEdit.text())
            self.statusLabel.setText("Connected")
            self.console.afegirMissatge("Connectat correctament a "+self.ipLineEdit.text())
            self.button.setText("Disconnect")
            self.status_connected=True
    
    def discover(self):
        self.console.afegirMissatge("Cercant Cameres a la xarxa...")
        self.discoverer.start()

    def printDiscoveries(self, ips):
        if not ips:
            self.console.afegirMissatge("No sha trobat res")
            pass
        for ip in ips:
            self.console.afegirMissatge("Sha trobat camara amb ip "+ip)
            self.ipline.setText(ip)


            



            
    

class Discoverer(QThread):
    discoveries=pyqtSignal(list)

    def __init__(self, console, ipline) -> None:
        super().__init__()
        self.console = console
        self.ipline = ipline
        pass

    # Quan s'apreta el botó de Discover
    def run(self):
        ips, uri = OnvifDiscovery("255.255.255.255")
        self.discoveries.emit(ips)
        