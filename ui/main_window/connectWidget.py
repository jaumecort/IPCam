# Form implementation generated from reading ui file '.\ui\dev\connectWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(80, 60, 211, 101))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 198, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.disconnectButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout.addWidget(self.disconnectButton, 1, 2, 1, 1)
        self.connectButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 1, 1, 1, 1)
        self.actionConnect = QtGui.QAction(parent=Form)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtGui.QAction(parent=Form)
        self.actionDisconnect.setObjectName("actionDisconnect")

        self.retranslateUi(Form)
        self.connectButton.clicked.connect(self.actionConnect.trigger) # type: ignore
        self.disconnectButton.clicked.connect(self.actionDisconnect.trigger) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Connect"))
        self.label_2.setText(_translate("Form", "status:"))
        self.label.setText(_translate("Form", "disconnected"))
        self.disconnectButton.setText(_translate("Form", "Disconnect"))
        self.connectButton.setText(_translate("Form", "Connect"))
        self.actionConnect.setText(_translate("Form", "Connect"))
        self.actionConnect.setToolTip(_translate("Form", "Connect to Camera"))
        self.actionDisconnect.setText(_translate("Form", "Disconnect"))
        self.actionDisconnect.setToolTip(_translate("Form", "Disconnect to camera"))