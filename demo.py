# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './design/first_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

path = "rtsp://admin:Admin123@192.168.111.210/1"
width = 720
height = 480
w_width = 1080
w_height = 700

class Thread(QtCore.QThread):
    changePixmap = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent):
        QtCore.QThread.__init__(self, parent)
        self._go = None

    def run(self):
        global path, width, height
        # run mode variable
        self._go = True
        cap = cv2.VideoCapture(path)
        while self._go:
            ret, frame = cap.read()
            # display on APP
            result_frame = cv2.resize(frame, (width, height))
            rgbImage = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
            h_result_frame, w_result_frame, ch = rgbImage.shape
            bytesPerLine = ch * w_result_frame
            convertToQtFormat = QtGui.QImage(rgbImage.data, w_result_frame, h_result_frame,
                                             bytesPerLine, QtGui.QImage.Format_RGB888)
            p = convertToQtFormat.scaled(width, height, QtCore.Qt.KeepAspectRatio)
            self.changePixmap.emit(p)

    def stop_thread(self):
        self._go = False


def close_window():
    global th
    th.stop_thread()


def restore(settings):
    finfo = QtCore.QFileInfo(settings.fileName())
    if finfo.exists() and finfo.isFile():
        for w in QtWidgets.qApp.allWidgets():
            mo = w.metaObject()
            if w.objectName() and not w.objectName().startswith("qt_"):
                settings.beginGroup(w.objectName())
                for i in range(mo.propertyCount(), mo.propertyOffset() - 1, -1):
                    prop = mo.property(i)
                    if prop.isWritable():
                        name = prop.name()
                        val = settings.value(name, w.property(name))
                        if str(val).isdigit():
                            val = int(val)
                        w.setProperty(name, val)
                settings.endGroup()


def save(settings):
    for w in QtWidgets.qApp.allWidgets():
        mo = w.metaObject()
        if w.objectName() and not w.objectName().startswith("qt_"):
            settings.beginGroup(w.objectName())
            for i in range(mo.propertyCount()):
                prop = mo.property(i)
                name = prop.name()
                if prop.isWritable():
                    settings.setValue(name, w.property(name))
            settings.endGroup()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1071, 651))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 720, 480))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(740, 10, 321, 501))
        self.groupBox.setObjectName("groupBox")
        self.person_image_1 = QtWidgets.QLabel(self.groupBox)
        self.person_image_1.setGeometry(QtCore.QRect(10, 30, 64, 64))
        self.person_image_1.setFrameShape(QtWidgets.QFrame.Box)
        self.person_image_1.setAlignment(QtCore.Qt.AlignCenter)
        self.person_image_1.setObjectName("person_image_1")
        self.person_image_2 = QtWidgets.QLabel(self.groupBox)
        self.person_image_2.setGeometry(QtCore.QRect(10, 110, 64, 64))
        self.person_image_2.setFrameShape(QtWidgets.QFrame.Box)
        self.person_image_2.setAlignment(QtCore.Qt.AlignCenter)
        self.person_image_2.setObjectName("person_image_2")
        self.person_image_3 = QtWidgets.QLabel(self.groupBox)
        self.person_image_3.setGeometry(QtCore.QRect(10, 190, 64, 64))
        self.person_image_3.setFrameShape(QtWidgets.QFrame.Box)
        self.person_image_3.setAlignment(QtCore.Qt.AlignCenter)
        self.person_image_3.setObjectName("person_image_3")
        self.person_image_4 = QtWidgets.QLabel(self.groupBox)
        self.person_image_4.setGeometry(QtCore.QRect(10, 270, 64, 64))
        self.person_image_4.setFrameShape(QtWidgets.QFrame.Box)
        self.person_image_4.setAlignment(QtCore.Qt.AlignCenter)
        self.person_image_4.setObjectName("person_image_4")
        self.person_image_5 = QtWidgets.QLabel(self.groupBox)
        self.person_image_5.setGeometry(QtCore.QRect(10, 350, 64, 64))
        self.person_image_5.setFrameShape(QtWidgets.QFrame.Box)
        self.person_image_5.setAlignment(QtCore.Qt.AlignCenter)
        self.person_image_5.setObjectName("person_image_5")
        self.person_infor_1 = QtWidgets.QLabel(self.groupBox)
        self.person_infor_1.setGeometry(QtCore.QRect(90, 30, 221, 61))
        self.person_infor_1.setFrameShape(QtWidgets.QFrame.Box)
        self.person_infor_1.setObjectName("person_infor_1")
        self.person_infor_2 = QtWidgets.QLabel(self.groupBox)
        self.person_infor_2.setGeometry(QtCore.QRect(90, 110, 221, 61))
        self.person_infor_2.setFrameShape(QtWidgets.QFrame.Box)
        self.person_infor_2.setObjectName("person_infor_2")
        self.person_infor_3 = QtWidgets.QLabel(self.groupBox)
        self.person_infor_3.setGeometry(QtCore.QRect(90, 190, 221, 61))
        self.person_infor_3.setFrameShape(QtWidgets.QFrame.Box)
        self.person_infor_3.setObjectName("person_infor_3")
        self.person_infor_4 = QtWidgets.QLabel(self.groupBox)
        self.person_infor_4.setGeometry(QtCore.QRect(90, 270, 221, 61))
        self.person_infor_4.setFrameShape(QtWidgets.QFrame.Box)
        self.person_infor_4.setObjectName("person_infor_4")
        self.person_infor_5 = QtWidgets.QLabel(self.groupBox)
        self.person_infor_5.setGeometry(QtCore.QRect(90, 350, 221, 61))
        self.person_infor_5.setFrameShape(QtWidgets.QFrame.Box)
        self.person_infor_5.setObjectName("person_infor_5")
        self.person_image_6 = QtWidgets.QLabel(self.groupBox)
        self.person_image_6.setGeometry(QtCore.QRect(10, 430, 64, 64))
        self.person_image_6.setFrameShape(QtWidgets.QFrame.Box)
        self.person_image_6.setAlignment(QtCore.Qt.AlignCenter)
        self.person_image_6.setObjectName("person_image_6")
        self.person_infor_6 = QtWidgets.QLabel(self.groupBox)
        self.person_infor_6.setGeometry(QtCore.QRect(90, 430, 221, 61))
        self.person_infor_6.setFrameShape(QtWidgets.QFrame.Box)
        self.person_infor_6.setObjectName("person_infor_6")
        self.start = QtWidgets.QPushButton(self.tab)
        self.start.setGeometry(QtCore.QRect(750, 530, 141, 81))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.tab)
        self.stop.setGeometry(QtCore.QRect(910, 530, 141, 81))
        self.stop.setObjectName("stop")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 500, 721, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 17))
        self.label_2.setObjectName("label_2")
        self.input_process_id = QtWidgets.QLineEdit(self.groupBox_2)
        self.input_process_id.setGeometry(QtCore.QRect(130, 70, 471, 25))
        self.input_process_id.setObjectName("input_process_id")
        self.input_camera_address = QtWidgets.QLineEdit(self.groupBox_2)
        self.input_camera_address.setGeometry(QtCore.QRect(130, 30, 471, 25))
        self.input_camera_address.setText("")
        self.input_camera_address.setObjectName("input_camera_address")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 121, 17))
        self.label_3.setObjectName("label_3")
        self.input = QtWidgets.QPushButton(self.groupBox_2)
        self.input.setGeometry(QtCore.QRect(620, 30, 89, 71))
        self.input.setObjectName("input")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 561, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 67, 21))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 71, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 30, 71, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 431, 25))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 67, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 91, 41))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 431, 25))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 140, 431, 25))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(60, 180, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 180, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # events
        # start video
        self.start.clicked.connect(self.video)
        # stop video
        self.stop.clicked.connect(close_window)
        global th
        th = Thread(MainWindow)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def video(self):
        global width, height
        self.label.resize(width, height)
        th.changePixmap.connect(self.setImage)
        th.start()

    def setImage(self, image):
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Display video"))
        self.groupBox.setTitle(_translate("MainWindow", "Information"))
        self.person_image_1.setText(_translate("MainWindow", "image_1"))
        self.person_image_2.setText(_translate("MainWindow", "image_2"))
        self.person_image_3.setText(_translate("MainWindow", "image_3"))
        self.person_image_4.setText(_translate("MainWindow", "image_4"))
        self.person_image_5.setText(_translate("MainWindow", "image_5"))
        self.person_infor_1.setText(_translate("MainWindow", "name_1"))
        self.person_infor_2.setText(_translate("MainWindow", "name_2"))
        self.person_infor_3.setText(_translate("MainWindow", "name_3"))
        self.person_infor_4.setText(_translate("MainWindow", "name_4"))
        self.person_infor_5.setText(_translate("MainWindow", "name_5"))
        self.person_image_6.setText(_translate("MainWindow", "image_6"))
        self.person_infor_6.setText(_translate("MainWindow", "name_6"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Source"))
        self.label_2.setText(_translate("MainWindow", "Process ID"))
        self.label_3.setText(_translate("MainWindow", "Camera Address"))
        self.input.setText(_translate("MainWindow", "INPUT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Register"))
        self.label_4.setText(_translate("MainWindow", "Path"))
        self.radioButton.setText(_translate("MainWindow", "Image"))
        self.radioButton_2.setText(_translate("MainWindow", "Video"))
        self.label_5.setText(_translate("MainWindow", "User ID"))
        self.label_6.setText(_translate("MainWindow", "Person name"))
        self.pushButton.setText(_translate("MainWindow", "APPLY"))
        self.pushButton_2.setText(_translate("MainWindow", "REGISTER"))
        self.pushButton_3.setText(_translate("MainWindow", "CANCEL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        global w_height, w_width
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(w_width, w_height)
        self.settings = QtCore.QSettings()
        # restore(self.settings)

    def closeEvent(self, event):
        save(self.settings)
        super().closeEvent(event)


if __name__ == '__main__':
    print("(***)--- Running APP threading")
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("Eyllanesc")
    QtCore.QCoreApplication.setOrganizationDomain("eyllanesc.com")
    QtCore.QCoreApplication.setApplicationName("MyApp")
    w = MainWindow()
    w.show()
    app.exec_()
