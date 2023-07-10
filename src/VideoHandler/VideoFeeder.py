import cv2

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

#from ui.main_window.MainWindow import MainWindow as mw

class VideoFeeder(QThread):
    changePixmap = pyqtSignal(QImage)
    feeding = False
    uri = 0
    label = None


    def setFeeding(self, b, label, uri=None):
        self.feeding = b
        self.label:QLabel = label
        if uri is not None:
            self.uri = uri
            
    def run(self):
        #print("rebent feed de: "+ str(self.uri))
        if self.uri=='0': self.uri=0
        cap = cv2.VideoCapture(self.uri)
        #while True:
        
        while self.feeding:
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
                p = convertToQtFormat.scaled(640, 360, Qt.AspectRatioMode.KeepAspectRatio)
                #prova per fer feed dinamic
                p = convertToQtFormat.scaled(self.label.width(), self.label.height(), Qt.AspectRatioMode.KeepAspectRatio)
                self.label.setPixmap(QPixmap.fromImage(p))