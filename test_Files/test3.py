# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate,Qt
import sys


class Ui_Form(QtWidgets.QWidget, QtCore.QTimer):



    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(1133, 658)
        Form.setWindowFlags(Form.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0.011, stop:0.0227273 rgba(0, 0, 28, 255), stop:0.977273 rgba(0, 0, 39, 255))")
        
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(860, 170, 241, 141))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 50)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_time = QtWidgets.QLabel(self.frame)
        self.label_time.setGeometry(QtCore.QRect(50, 70, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 31, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("photos/79-795942_or-tool-svg-png-icon-free-download-clock.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(60, 20, 181, 41))
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(860, 370, 241, 141))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 50)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 20, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photos/Calories_Burned_-fire-Calories_Burn-Burn-Metabolism-512.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(90, 20, 111, 41))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_calories = QtWidgets.QLabel(self.frame_2)
        self.label_calories.setGeometry(QtCore.QRect(80, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(48)
        self.label_calories.setFont(font)
        self.label_calories.setObjectName("label_calories")
        
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(40, 310, 371, 141))
        self.frame_3.setStyleSheet("background-color: rgb(0, 0, 50)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_distance = QtWidgets.QLabel(self.frame_3)
        self.label_distance.setGeometry(QtCore.QRect(190, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_distance.setFont(font)
        self.label_distance.setTextFormat(QtCore.Qt.RichText)
        self.label_distance.setObjectName("label_distance")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 191, 141))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("photos/road-icon-on-white-background-vector-21154187.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(220, 30, 111, 41))
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(290, 60, 61, 51))
        self.label_10.setObjectName("label_10")
        
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(40, 500, 371, 131))
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 50)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(100, 20, 71, 41))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("photos/600-6003521_ketond-keto-supplements-com-agility-icon-png-transparent.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(180, 70, 91, 51))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 91, 41))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_speed = QtWidgets.QLabel(self.frame_4)
        self.label_speed.setGeometry(QtCore.QRect(100, 70, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        self.label_speed.setFont(font)
        self.label_speed.setTextFormat(QtCore.Qt.RichText)
        self.label_speed.setObjectName("label_speed")
        
        self.pushButton_speed_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_speed_2.setGeometry(QtCore.QRect(290, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(28)
        self.pushButton_speed_2.setFont(font)
        self.pushButton_speed_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_speed_2.setStyleSheet("color: rgb(255, 255, 0);\n""border-width: 3px;\n""border-style: solid;\n""border-color: rgb(255, 255, 0);\n""border-radius: 25px;")
        self.pushButton_speed_2.setObjectName("pushButton_speed_2")
        
        self.pushButton_speed_1 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_speed_1.setGeometry(QtCore.QRect(20, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(28)
        self.pushButton_speed_1.setFont(font)
        self.pushButton_speed_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_speed_1.setStyleSheet("color: rgb(255, 255, 0);\n""border-width: 3px;\n""border-style: solid;\n""border-color: rgb(255, 255, 0);\n""border-radius: 25px;")
        self.pushButton_speed_1.setObjectName("pushButton_speed_1")
        
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(690, 570, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start.setStyleSheet("color: white;\n""border-width: 3px;\n""border-style: solid;\n""border-color: red;\n""border-radius: 20px;")
        self.pushButton_start.setObjectName("pushButton_start")
        
        self.pushButton_stop = QtWidgets.QPushButton(Form)
        self.pushButton_stop.setGeometry(QtCore.QRect(910, 570, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_stop.setStyleSheet("color: white;\n""border-width: 3px;\n""border-style: solid;\n""border-color:rgb(255, 255, 0) ;\n""border-radius: 20px;")
        self.pushButton_stop.setObjectName("pushButton_stop")
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(450, 120, 381, 421))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setPixmap(QtGui.QPixmap("photos/man-running.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(40, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: white;")
        self.label_12.setTextFormat(QtCore.Qt.RichText)
        self.label_12.setObjectName("label_12")
        
        self.pushButton_speed_3 = QtWidgets.QPushButton(Form)
        self.pushButton_speed_3.setGeometry(QtCore.QRect(950, 30, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(28)
        self.pushButton_speed_3.setFont(font)
        self.pushButton_speed_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_speed_3.setStyleSheet("color: rgb(255, 255, 0);\n""border-width: 3px;\n""border-style: solid;\n""border-color: rgb(255, 110, 31);\n""border-radius: 25px;")
        self.pushButton_speed_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos/settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_speed_3.setIcon(icon)
        self.pushButton_speed_3.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_speed_3.setObjectName("pushButton_speed_3")
        
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(60, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: white;")
        self.label_13.setObjectName("label_13")
        
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(470, 570, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_add.setStyleSheet("color: white;\n""border-width: 3px;\n""border-style: solid;\n""border-color: rgb(85, 0, 255);\n""border-radius: 20px;")
        self.pushButton_add.setObjectName("pushButton_add")
        
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(40, 120, 371, 151))
        self.frame_5.setStyleSheet("background-color: rgb(0, 0, 50)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(140, 10, 201, 41))
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.label_steps = QtWidgets.QLabel(self.frame_5)
        self.label_steps.setGeometry(QtCore.QRect(200, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_steps.setFont(font)
        self.label_steps.setObjectName("label_steps")
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(20, 20, 111, 111))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("photos/feet-clipart-blue-foot-foot-icon-png-transparent.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(280, 30, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("color: white;\n""background-color: rgb(0, 0, 50);\n""border: 3px solid ;\n""border-color: rgb(0, 0, 50)")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        
        self.pushButton_speed_4 = QtWidgets.QPushButton(Form)
        self.pushButton_speed_4.setGeometry(QtCore.QRect(1020, 30, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(28)
        self.pushButton_speed_4.setFont(font)
        self.pushButton_speed_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_speed_4.setStyleSheet("color: rgb(255, 255, 0);\n""border-width: 3px;\n""border-style: solid;\n""border-color:rgb(224, 0, 36);\n""border-radius: 25px;")
        self.pushButton_speed_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photos/kisspng-computer-icons-shutdown-internet-computer-software-quit-5ad8d713227452.1198148915241602751411.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_speed_4.setIcon(icon1)
        self.pushButton_speed_4.setIconSize(QtCore.QSize(63, 68))
        self.pushButton_speed_4.setObjectName("pushButton_speed_4")

        # button command
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_start.clicked.connect(self.speedDisplay)
        self.pushButton_start.clicked.connect(self.realTime)

        self.pushButton_stop.clicked.connect(self.realEnd)

        self.pushButton_speed_2.clicked.connect(self.speedUp)
        self.pushButton_speed_1.clicked.connect(self.speedDown)

        self.pushButton_speed_4.clicked.connect(self.exit)
        # button command

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        timer = QTimer(self)
        timer.timeout.connect(self.realDisplay)
        timer.start(1000)


    RPM = 40
    radius = 0.09 # meter
    weight = 50 # kg
    height = 1.43 # meter
    target = 100 # meter
    gender = "female"

    second = 0
    minute = 0
    hour = 0
    run = False
    system = False

    speed = (2 * 3.14 * radius * RPM * 3.6) / 60 # km/h "must change"
    DistancePersecond = speed / 3600 # km
    # numOfStep = 2 * (( 5280 / ( height * 0.413 * 39.37 / 12 ) ) * ( Distance / 1609.344 ))
    # CaloriesBurntPerSecond  = (( 0.035 * weight ) + (( (speed/3.6)**2 / height ) * 0.029 * weight )) * 1 / 60

    def add(self):
        if __name__ == "__main__":
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            Form.close()
            self.MainWindow.show()

    def exit(self):
        Form.close()


    def realEnd(self):
        self.run = False
        self.pushButton_start.setText("START")

        self.label_steps.setText("0")
        self.label_steps.setStyleSheet("color: white;")

        self.label_distance.setText("0.000")
        self.label_distance.setStyleSheet("color: white;")

        self.label_calories.setText("0.0")
        self.label_calories.setStyleSheet("color: white;")

        self.label_time.setText("00:00:00")

        self.progressBar.setValue(0)

        self.label_3.setPixmap(QtGui.QPixmap("photos/man-running.gif"))

        self.second = 0
        self.minute = 0
        self.hour = 0
        self.DistancePersecond = self.speed / 3600
        self.run = False
        self.system = False


    def realTime(self):
        print("clicked")

        if self.gender == "male" :
            self.movie = QtGui.QMovie("photos/source (1).gif")
            self.label_3.setMovie(self.movie)
            self.movie.start()
        else :
            self.movie = QtGui.QMovie("photos/source.gif")
            self.label_3.setMovie(self.movie)
            self.movie.start()

        self.pushButton_start.setText("STOP")
        if self.system :
            self.pushButton_start.setText("RESUME")
            self.system = False
            self.run = False

            if self.gender == "male" :
                self.label_3.setPixmap(QtGui.QPixmap("photos/source (1).gif"))
            else:
                self.label_3.setPixmap(QtGui.QPixmap("photos/source.gif"))
        else:
            self.system = True
            self.run = True 


    def realDisplay(self):
        if self.run :
            self.DistancePersecond = self.DistancePersecond + (self.speed / 3600 )
   
            self.second = self.second + 1
            if self.second >= 59 :
                self.minute = self.minute + 1
                self.second = 0
                if self.minute >= 59 :
                    self.hour = self.hour + 1
                    self.minute = 0


            time = "{:02d}".format(self.hour) + ":" + "{:02d}".format(self.minute) + ":" + "{:02d}".format(self.second)
            self.label_time.setStyleSheet("color: white")
            self.label_time.setText(time)

            self.label_distance.setText("{:.3f}".format(self.DistancePersecond))
            self.label_distance.setStyleSheet("color: white;")

            numStep = 2 * (( 5280 / ( self.height * 0.413 * 39.37 / 12 ) ) * ( self.DistancePersecond / 1.609344 ))
            self.label_steps.setText("{:.0f}".format(numStep))
            self.label_steps.setStyleSheet("color: white;")

            self.progressBar.setValue(int(self.DistancePersecond * 1000 * 100 / self.target))


    def speedDisplay(self):
        speedOneDesci = "{:.2f}".format(self.speed)
        self.label_speed.setStyleSheet("color: white;")
        self.label_speed.setText(speedOneDesci)


    def speedDown(self):
        currentSpeed = "{:.2f}".format(self.speed)
        newSpeed = float(currentSpeed) - 0.01
        self.speed = newSpeed
        self.label_speed.setStyleSheet("color: white;")
        self.label_speed.setText(str(newSpeed))


    def speedUp(self,num):
        currentSpeed = "{:.2f}".format(self.speed)
        newSpeed = float(currentSpeed) + 0.01
        self.speed = newSpeed
        self.label_speed.setStyleSheet("color: white;")
        self.label_speed.setText(str(newSpeed))


    def showTime(self):
        currentTime = QTime.currentTime()
        displayTime = currentTime.toString(Qt.DefaultLocaleLongDate)
        self.label_13.setText(displayTime)
        currentDate = QDate.currentDate()
        self.label_12.setText(currentDate.toString(Qt.DefaultLocaleLongDate))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Treadmill Software"))
        self.label_time.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">00:00:00</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">SESSION TIME</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">CALORIES</span></p></body></html>"))
        self.label_calories.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0.0</span></p></body></html>"))
        self.label_distance.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0.000</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">DISTANCE</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">km</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">km/h</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">SPEED</span></p></body></html>"))
        self.label_speed.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0.00</span></p></body></html>"))
        self.pushButton_speed_2.setText(_translate("Form", ">"))
        self.pushButton_speed_1.setText(_translate("Form", "<"))
        self.pushButton_start.setText(_translate("Form", "START"))
        self.pushButton_stop.setText(_translate("Form", "RESET"))
        self.label_12.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Wednesday, Desember 8, 2020</span></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">00:0:00 AM</span></p></body></html>"))
        self.pushButton_add.setText(_translate("Form", "ADD"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">NUMBER OF STEPS</span></p></body></html>"))
        self.label_steps.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())