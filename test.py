# from PyQt5 import QtCore, QtGui, QtWidgets 
# import sys 

# class Ui_MainWindow(QtWidgets.QWidget): 
# 	def setupUi(self, MainWindow): 
# 		MainWindow.resize(422, 255) 
# 		self.centralwidget = QtWidgets.QWidget(MainWindow) 

# 		self.pushButton = QtWidgets.QPushButton(self.centralwidget) 
# 		self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28)) 

# 		# For displaying confirmation message along with user's info. 
# 		self.label = QtWidgets.QLabel(self.centralwidget)	 
# 		self.label.setGeometry(QtCore.QRect(170, 40, 201, 111)) 

# 		# Keeping the text of label empty initially.	 
# 		self.label.setText("")	 

# 		MainWindow.setCentralWidget(self.centralwidget) 
# 		self.retranslateUi(MainWindow) 
# 		QtCore.QMetaObject.connectSlotsByName(MainWindow) 

# 	def retranslateUi(self, MainWindow): 
# 		_translate = QtCore.QCoreApplication.translate 
# 		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) 
# 		self.pushButton.setText(_translate("MainWindow", "Proceed")) 
# 		self.pushButton.clicked.connect(self.takeinputs) 
		
# 	def takeinputs(self): 
# 		name, done1 = QtWidgets.QInputDialog.getText( 
# 			self, 'Input Dialog', 'Enter your name:') 

# 		roll, done2 = QtWidgets.QInputDialog.getInt( 
# 		self, 'Input Dialog', 'Enter your roll:') 

# 		cgpa, done3 = QtWidgets.QInputDialog.getDouble( 
# 			self, 'Input Dialog', 'Enter your CGPA:') 

# 		langs =['C', 'c++', 'Java', 'Python', 'Javascript'] 
# 		lang, done4 = QtWidgets.QInputDialog.getItem( 
# 		self, 'Input Dialog', 'Language you know:', langs) 

# 		if done1 and done2 and done3 and done4 : 
# 			# Showing confirmation message along 
# 			# with information provided by user. 
# 			self.label.setText('Information stored Successfully\nName: '
# 								+str(name)+'('+str(roll)+')'+'\n'+'CGPA: '
# 								+str(cgpa)+'\nSelected Language: '+str(lang)) 

# 			# Hide the pushbutton after inputs provided by the use. 
# 			self.pushButton.hide()	 
				
			
			
# if __name__ == "__main__": 
# 	app = QtWidgets.QApplication(sys.argv) 
# 	MainWindow = QtWidgets.QMainWindow() 
# 	ui = Ui_MainWindow() 
# 	ui.setupUi(MainWindow) 
# 	MainWindow.show()  

# 	sys.exit(app.exec_()) 




# from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)
# import sys

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # Add button                                                                                                     
#         self.btn = QPushButton('Show Input Dialog', self)
#         self.btn.move(30, 20)
#         self.btn.clicked.connect(self.showDialog)

# 	# Add label                                                                                                      
#         self.le = QLabel(self)
#         self.le.move(30, 62)
#         self.le.resize(400,22)
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Input dialog')
#         self.show()


#     def showDialog(self):
#     	text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter text:')
#     	if ok:
#     		self.le.setText(str(text))

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
 
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
 
        layout = QVBoxLayout()
 
        fnt = QFont('Open Sans', 120, QFont.Bold)
 
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFont(fnt)
        layout.addWidget(self.lbl)
 
        self.setLayout(layout)
 
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # update every second
 
        self.showTime()
 
    def showTime(self):
        currentTime = QTime.currentTime()
 
        displayTxt = currentTime.toString('hh:mm:ss')
        print(displayTxt)
 
        self.lbl.setText(displayTxt)
 
 
app = QApplication(sys.argv)
 
demo = AppDemo()
demo.show()
 
app.exit(app.exec_())