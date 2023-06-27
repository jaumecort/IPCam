import cv2

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from VideoHandler.VideoFeeder import *

class FeedBox():
    vf = VideoFeeder()

    def setImage(self, image):
        self.labelVideo.setPixmap(QPixmap.fromImage(image))

    def __init__(self, mainwindow) -> None:
        # Init accesos a mainwindow
        self.labelVideo = mainwindow.labelVideo
        self.ipline = mainwindow.ipLineEdit

        # Init signals
        self.vf.changePixmap.connect(self.setImage)

        # Init Objectes
        self.vf.setFeeding(False, self.labelVideo)

        pass

    def startFeed(self, uri):
        self.vf.setFeeding(True, self.labelVideo, uri)
        self.vf.start()

    def stopFeed(self):
        self.vf.setFeeding(False, self.labelVideo)

    