import typing

from OnvifController.PTZController import PTZController

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *



class PTZBox:
    status_connected=False
    def __init__(self, mainwindow) -> None:
        ## Init de tots als accessos a MainWindow
        self.buttonUp:QToolButton = mainwindow.PTZup
        self.buttonDown:QToolButton = mainwindow.PTZdown
        self.buttonLeft:QToolButton = mainwindow.PTZleft
        self.buttonRigth:QToolButton = mainwindow.PTZrigth
        self.buttonZIn:QPushButton = mainwindow.PTZIn
        self.buttonZout:QPushButton = mainwindow.PTZout
        self.console=mainwindow.consoleBox
        self.ptzbox=mainwindow.PTZBox
        
        ## Init de les senyals necessaries
        mainwindow.actionPTZup.triggered.connect(self.moveup)
        mainwindow.actionPTZdown.triggered.connect(self.movedown)
        mainwindow.actionPTZleft.triggered.connect(self.moveleft)
        mainwindow.actionPTZright.triggered.connect(self.moveright)
        #mainwindow.actionPTZin.triggered.connect(self.zoomin)
        #mainwindow.actionPTZout.triggered.connect(self.zoomout)
        mainwindow.actionPTZstop.triggered.connect(self.stop)

        self.ptzSender = None
        pass

    def connectPTZ(self, cam):
        try:
            self.ptzSender = PTZController(cam)
            self.console.afegirMissatge("PTZ conected")
            self.ptzbox.setEnabled(True)
        except: 
            self.ptzSender = None
            self.console.afegirMissatge("PTZ not conected!")

    def disconnectPTZ(self):
        self.ptzSender = None
        self.console.afegirMissatge("PTZ disconected")
        self.ptzbox.setEnabled(False)

    # Quan s'apreta el botó de Up
    def moveup(self):
        if(self.ptzSender is not None):
            self.ptzSender.move_up()

    def movedown(self):
        if(self.ptzSender is not None):
            self.ptzSender.move_down()

    def moveleft(self):
        if(self.ptzSender is not None):
            self.ptzSender.move_left()

    def moveright(self):
        if(self.ptzSender is not None):
            self.ptzSender.move_right()

    def stop(self):
        if(self.ptzSender is not None):
            self.ptzSender.stop()
        else:
            self.console.afegirMissatge("PTZ not conected!")



