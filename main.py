
import sys
import re
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainView(QMainWindow):

	ONE_NUMBER 		= '^[0-9]$'
	EIGHT_NUMBERS 	= '^[0-9]{8}$'

	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("calculator.ui", self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Basic Calculator")

		self.lcdAnswer.display(0)

		self.btnAllClear.clicked.connect(self.allClear)
		self.btnClear.clicked.connect(self.clear)

		self.btn0.clicked.connect(self.addNum0)
		self.btn1.clicked.connect(self.addNum1)
		self.btn2.clicked.connect(self.addNum2)
		self.btn3.clicked.connect(self.addNum3)
		self.btn4.clicked.connect(self.addNum4)
		self.btn5.clicked.connect(self.addNum5)
		self.btn6.clicked.connect(self.addNum6)
		self.btn7.clicked.connect(self.addNum7)
		self.btn8.clicked.connect(self.addNum8)
		self.btn9.clicked.connect(self.addNum9)

	def allClear(self):
		self.lcdAnswer.display(0)

	def clear(self):
		pat = re.compile(self.ONE_NUMBER)
		num = str(int(self.lcdAnswer.value()))
		if pat.match(num):
			self.allClear()
		else:
			tex = num[:-1]
			self.lcdAnswer.display(str(tex))

	def isEqual0(self):
		return self.lcdAnswer.value() == 0

	def isFull(self):
		pat = re.compile(self.EIGHT_NUMBERS)
		num = str(int(self.lcdAnswer.value()))
		return pat.match(num)

	def addNum0(self):
		if not self.isFull():
			if not self.isEqual0():
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'0')

	def addNum1(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(1)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'1')

	def addNum2(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(2)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'2')

	def addNum3(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(3)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'3')

	def addNum4(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(4)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'4')

	def addNum5(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(5)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'5')

	def addNum6(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(6)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'6')

	def addNum7(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(7)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'7')

	def addNum8(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(8)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'8')

	def addNum9(self):
		if not self.isFull():
			if self.isEqual0():
				self.lcdAnswer.display(9)
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'9')

app = QApplication(sys.argv)
window = MainView()
window.show()
app.exec_()