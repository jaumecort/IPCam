from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from onvif import ONVIFService

#from UI.MainWindow.MainWindow import MainWindow
from UI.DeviceManager.deviceManager_ui import *

class DeviceManager(QDialog, Ui_DeviceManager):

    cameraclient = None
    management_service:ONVIFService = None
    device_information = None
    dateandtime = None
    hostname = None

    def __init__(self, mw, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        mw.actionDevice_Management.triggered.connect(self.mostrar)
        self.applyButton.pressed.connect(self.apply_dades)
        self.exitButton.pressed.connect(self.close)
        self.datetimeButton.pressed.connect(self.updatedateandtime)

        self.disconsignal = mw.disconnectionSignal

        self.cameraclient = mw.cameraclient
        if self.cameraclient:
            self.management_service = mw.cameraclient.devicemgmt_service

    def updatedateandtime(self):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def print_dades(self):
        self.device_information = self.management_service.GetDeviceInformation()
        self.LabelManufacter.setText(self.device_information['Manufacturer'])
        self.LabelModel.setText(self.device_information['Model'])
        self.LabelFirmwareVersion.setText(self.device_information['FirmwareVersion'])
        self.LabelSerialNumber.setText(self.device_information['SerialNumber'])
        self.LabelHardwareID.setText(self.device_information['HardwareId'])

        self.dateandtime = self.management_service.GetSystemDateAndTime()
        self.comboDateTimeType.setCurrentText(self.dateandtime['DateTimeType'])
        self.checkDayLightSavings.setChecked(self.dateandtime['DaylightSavings'])
        date = self.dateandtime['UTCDateTime']['Date']
        time = self.dateandtime['UTCDateTime']['Time']
        t = QDateTime(date['Year'], date['Month'], date['Day'], time['Hour'], time['Minute'], time['Second'])
        self.dateTimeEdit.setDateTime(t)
        self.hostname = self.management_service.GetHostname()
        self.LineHostname.setText(self.hostname['Name'])

    def apply_dades(self):
        try:
            self.hostname = self.LineHostname.text()
            self.management_service.SetHostname(self.hostname)
            datetime = self.dateTimeEdit.dateTime()
            date = self.dateandtime['UTCDateTime']['Date']
            time = self.dateandtime['UTCDateTime']['Time']
            date['Year']=datetime.date().year()
            date['Month']=datetime.date().month()
            date['Day']=datetime.date().day()
            time['Hour']=datetime.time().hour()
            time['Minute']=datetime.time().minute()
            time['Second']=datetime.time().second()
            self.dateandtime['UTCDateTime']['Date'] = date
            self.dateandtime['UTCDateTime']['Time'] = time
            self.dateandtime['DaylightSavings'] = self.checkDayLightSavings.isChecked()
            self.dateandtime['DateTimeType'] = self.comboDateTimeType.currentText()
            setdatetime = {}
            setdatetime['DateTimeType']=self.dateandtime['DateTimeType']
            setdatetime['DaylightSavings']=self.dateandtime['DaylightSavings']
            setdatetime['TimeZone']=self.dateandtime['TimeZone']
            setdatetime['UTCDateTime']=self.dateandtime['UTCDateTime']
            self.management_service.SetSystemDateAndTime(setdatetime)
            self.close()
        except:
            QMessageBox.critical(None, "Exception","Unable to set this data")
    

    def mostrar(self):
        if self.cameraclient:
            try:
                self.management_service = self.cameraclient.devicemgmt_service
                self.print_dades()
                self.exec()
            except:
                QMessageBox.critical(None, "Exception","Unable to get data")
        else:
            QMessageBox.critical(None, "Conexion Error", "Any camera connected")