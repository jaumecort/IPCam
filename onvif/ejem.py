from PySide6.QtCore import Qt, QObject, Slot

class ejemp(QObject):
    def __init__(self):
        QObject.__init__(self)
    @Slot()
    def saludar(self):
        print('ola')