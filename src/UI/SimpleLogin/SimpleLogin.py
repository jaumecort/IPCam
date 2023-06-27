import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from UI.SimpleLogin.simple_login_ui import *


class SimpleLogin(QDialog,Ui_Dialog):

    username=''
    password=''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.Xbutton.clicked.connect(self.connectX)
        self.Ybutton.clicked.connect(self.connectY)


    def connectX(self):
        self.username = 'admin'
        self.password = 'L2F63400'
        self.close()
    
    def connectY(self):
        self.username = 'admin'
        self.password = 'L22E38E9'
        self.close()


    def getCredentials(self):
        return [self.username, self.password]
        
    @staticmethod
    def logindata():
        
        dialog = SimpleLogin()
        dialog.exec()
        return dialog.getCredentials()