from PyQt6 import QtCore, QtGui, QtWidgets
#from ui.main_window.MainWindow import MainWindow

class Follower(QtWidgets.QWidget):
    
    def setup(self, name):
        #self.Follower = QtWidgets.QWidget(parent=self.FollowersScrollAreaWidgetContents)
        self.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(300, 21))
        self.setMaximumSize(QtCore.QSize(300, 21))
        self.setObjectName(name)


        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0,0,0,0)

        self.FollowerCheck = QtWidgets.QCheckBox(parent=self)
        self.FollowerCheck.setObjectName("FollowerCheck")
        self.horizontalLayout.addWidget(self.FollowerCheck)
        self.FollowerTypeBox = QtWidgets.QComboBox(parent=self)
        self.FollowerTypeBox.setObjectName("FollowerTypeBox")
        self.FollowerTypeBox.addItem("")
        self.FollowerTypeBox.addItem("")
        self.FollowerTypeBox.addItem("")
        self.horizontalLayout.addWidget(self.FollowerTypeBox)
        self.FollowerLabelStatus = QtWidgets.QLabel(parent=self)
        self.FollowerLabelStatus.setObjectName("FollowerLabelStatus")
        self.horizontalLayout.addWidget(self.FollowerLabelStatus)
    

        _translate = QtCore.QCoreApplication.translate
        self.FollowerCheck.setText(_translate("MainWindow", "CheckBox"))
        self.FollowerTypeBox.setItemText(0, _translate("MainWindow", "Led"))
        self.FollowerTypeBox.setItemText(1, _translate("MainWindow", "Bombilla"))
        self.FollowerTypeBox.setItemText(2, _translate("MainWindow", "LCD"))
        self.FollowerLabelStatus.setText(_translate("MainWindow", "TextLabel"))
        