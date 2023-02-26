# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtCore import QTimer, QTime, Qt


class Ui_MainWindow(QtWidgets.QWidget, QtCore.QTimer):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 146)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 50, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

    # def show(self):
    #     msg = QMessageBox()
    #     msg.setWindowTitle("pyqy5")
    #     msg.setText("main text")

    #     x = msg.exec_()

    def show(self):
        # font = QtGui.QFont()
        # font.setPointSize(17)
        # font.color(red)
        # inputDialog = QtWidgets.QInputDialog()
        # inputDialog.setStyleSheet("background-color:black;\n""border-width: 1px;\n""border-style: solid;\n""border-color: rgb(255, 255, 0);")
        # inputDialog.setInputMode(QInputDialog.TextInput)
        # inputDialog.setWindowTitle("Input")
        # inputDialog.setLabelText("Enter the name for this new file:")
        # inputDialog.setFont(font)
        # ok = inputDialog.exec_()
        # print(inputDialog.textValue())
        # text, ok = QtWidgets.QInputDialog().getText(self, 'Input Dialog', "<FONT COLOR='#ff0000'>Enter number:</FONT>")
        # if ok:
        #     self.lineEdit.setText(str(text))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculate"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_2.setText(_translate("MainWindow", "+"))

    # def clicked(self):
    # 	x = self.lineEdit.text()
    # 	y = self.lineEdit_2.text()

    # 	z = float(x) + float(y)
    # 	print(z)
    # 	self.label.setText(x + " + " + y + " = " +str(z))
    # 	self.lineEdit.setText("")
    # 	self.lineEdit_2.setText("")

    def showTime(self):
        currentTime = QTime.currentTime()
        displayTxt = currentTime.toString('hh:mm:ss')
        print(displayTxt)
        self.label.setText(displayTxt)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
