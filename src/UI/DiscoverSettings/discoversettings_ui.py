# Form implementation generated from reading ui file '.\src\UI\DiscoverSettings\discover.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(251, 138)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(15, -1, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.bclineedit = QtWidgets.QLineEdit(parent=Dialog)
        self.bclineedit.setObjectName("bclineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bclineedit)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.timeoutbox = QtWidgets.QSpinBox(parent=Dialog)
        self.timeoutbox.setMinimum(1)
        self.timeoutbox.setMaximum(20)
        self.timeoutbox.setProperty("value", 3)
        self.timeoutbox.setObjectName("timeoutbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.timeoutbox)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exitButton = QtWidgets.QPushButton(parent=Dialog)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.applybutton = QtWidgets.QPushButton(parent=Dialog)
        self.applybutton.setObjectName("applybutton")
        self.horizontalLayout_2.addWidget(self.applybutton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Discover"))
        self.label_3.setText(_translate("Dialog", "Discovery Settings"))
        self.label.setText(_translate("Dialog", "Broadcast IP:"))
        self.bclineedit.setText(_translate("Dialog", "255.255.255.255"))
        self.label_2.setText(_translate("Dialog", "Timeout:"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.applybutton.setText(_translate("Dialog", "Apply"))
