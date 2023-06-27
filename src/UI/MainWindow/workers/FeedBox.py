import cv2

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

#from ui.main_window.MainWindow import MainWindow as mw

class FeedBox():
    def setImage(self, image):
        self.labelVideo.setPixmap(QPixmap.fromImage(image))

    def __init__(self, mainwindow) -> None:
        # Init accesos a mainwindow
        self.labelVideo = mainwindow.labelVideo
        self.ipline = mainwindow.ipLineEdit

        # Init Objectes
        self.vf = VideoFeeder()
        self.vf.setFeeding(False)

        # Init signals
        self.vf.changePixmap.connect(self.setImage)

        pass

    def startFeed(self, uri):
        self.vf.setFeeding(True, uri)
        self.vf.start()

    def stopFeed(self):
        self.vf.setFeeding(False)



class VideoFeeder(QThread):
    changePixmap = pyqtSignal(QImage)
    feeding = False
    uri = 0

    def setFeeding(self, b, uri=None):
        self.feeding = b
        if uri is not None:
            self.uri = uri
            
    def run(self):
        print("rebent feed de: "+ self.uri)
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
                self.changePixmap.emit(p)
    