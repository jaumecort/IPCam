# This Python file uses the following encoding: utf-8
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from UI.MainWindow.workers import *

from UI.MainWindow.main_window_ui import *

from UI.MainWindow.widgets import *



class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        #vf.start()
        # Aqui definirem els objectes necessaris:
        self.feedBox=FeedBox(self)
        self.consoleBox=ConsoleBox(self.console)
        self.cameraBox=CameraBox(self)
        
        
        #Setup ui i signals
        self.connectSignalsSlots()
    

        #Prova followers
        self.f = []
        for i in range(3):
            self.f.append(Follower(parent=self.FollowersScrollAreaWidgetContents))

        for fol in self.f:
            fol.setup("follower2")
            self.FollowersLayout.addWidget(fol)



    
        #Aqui connectarem totes les senyals amb funcions propies
    def connectSignalsSlots(self):
        #Boto discover
        
        #Boto connect
        self.actionConnection.triggered.connect(self.cameraBox.connect)
        #Senyal per canviar la imatge
    
        

    
    
        




