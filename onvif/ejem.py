from PyQt5.QtCore import Qt, QObject

class ejemp(QObject):
    def __init__(self):
        QObject.__init__(self)


    def saludar(self):
        print('ola')