# This Python file uses the following encoding: utf-8
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from UI.MainWindow.workers import *
from UI.MainWindow.workers.PTZBox import *

from UI.MainWindow.main_window_ui import *

from UI.MainWindow.widgets import *

from OnvifController.DeviceManager import *
from OnvifController.DiscoverSettings import *

from Tools.WebCamConnecter import *



class MainWindow(QMainWindow, Ui_MainWindow):

    connectionSignal=pyqtSignal(CameraClient)
    disconnectionSignal=pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Definim la camera
        self.cameraclient:CameraClient = None
        self.connectionSignal.connect(self.setConnection)
        self.disconnectionSignal.connect(self.setdisConnection)
        
        self.DiscovererSettings = DiscovererSettings(self)


        #vf.start()
        # Aqui definirem les Boxes
        self.cameraBox=None
        self.consoleBox=ConsoleBox(self.console)
        self.ptzBox=PTZBox(self)
        self.feedBox=FeedBox(self)
        self.cameraBox=CameraBox(self)

        # Aqui les eines de la barra
        self.DeviceManager = DeviceManager(self)
        self.webcamConnecter = WebCamConnecter(self)

        


        #Prova followers
        # self.f = []
        # for i in range(3):
        #     self.f.append(Follower(parent=self.FollowersScrollAreaWidgetContents))

        # for fol in self.f:
        #     fol.setup("follower2")
        #     self.FollowersLayout.addWidget(fol)


   
    def setConnection(self, client:CameraClient):
        self.cameraclient = client     
        self.cameraBox.status_connected = True
        self.DeviceManager.cameraclient = client
        try:
            self.feedBox.startFeed(self.cameraclient.getStreamUri())
        except Exception as e:
            ConsoleBox.afegirMissatge(str(e))
        try:
            self.ptzBox.connectPTZ(self.cameraclient.mycam)
        except:
            ConsoleBox.afegirMissatge("PTZ not found")

    def setdisConnection(self):
        self.cameraBox.status_connected = False
        self.cameraBox.layout_disconnect()
        self.cameraclient = None     
        self.DeviceManager.cameraclient = None
        self.feedBox.stopFeed()
        self.ptzBox.disconnectPTZ()


    
    
        




