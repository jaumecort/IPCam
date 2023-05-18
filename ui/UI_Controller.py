# This Python file uses the following encoding: utf-8
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.main_window.main_window_ui import Ui_MainWindow

from development.OnvifDiscovery.OnvifDiscoverer import OnvifDiscovery

class UI_Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.threadpool = QThreadPool()
        print("Multithreading UI with maximum %d threads" % self.threadpool.maxThreadCount())

    def connectSignalsSlots(self):
        self.actionDiscover.triggered.connect(self.connect)
        #self.actionConnection.triggered.connect(Connecter.connect())

    def connect(self):
        ip = self.ipedit.text()
        [ips, uris] = OnvifDiscovery(ip)
        self.name.setText(ips[0])

    def about(self):
        QMessageBox.about(
            self,

            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )



