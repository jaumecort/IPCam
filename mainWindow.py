# This Python file uses the following encoding: utf-8
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *


from main_window_ui import Ui_MainWindow

from onvif import ONVIFCamera
from development.PTZController.PTZController import PTZController

class Connecter(QRunnable):
    '''
    Worker thread
    '''

    @pyqtSlot()
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Thread start")
        try:
            mycam = ONVIFCamera("19", 80, 'admin', 'L2F63400', 'etc/onvif/wsdl/')
        except:
                print("Fail")
        print("Thread complete")

    

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def connectSignalsSlots(self):
        self.actionconnecting.triggered.connect(self.connecting)
        self.actionAbout.triggered.connect(self.about)

    def connecting(self):
        self.connectionLabel.setText("Connecting")
        ip = self.ip.text()
        worker = Connecter()
        self.threadpool.start(worker)
        self.connectionLabel.setText(ip)
        

    def about(self):
        QMessageBox.about(
            self,

            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )



if __name__ == "__main__":
    #mycam = ONVIFCamera('192.168.88.253', 80, 'admin', 'L2F63400', 'etc/onvif/wsdl/')
    #ptz = PTZController(mycam)

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
