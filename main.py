
import sys
import re
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainView(QMainWindow):

	ONE_NUMBER 		= '^[0-9]$'
	EIGHT_NUMBERS 	= '^[0-9]{8}$'

	global firstNum
	global thereOperation
	global symbol

	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("calculator.ui", self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Basic Calculator")

		self.lcdAnswer.display(0)

		self.btnAllClear.clicked.connect(self.allClear)
		self.btnClear.clicked.connect(self.clear)

		self.btnPlus.clicked.connect(self.addButton)
		self.btnMinus.clicked.connect(self.subButton)
		self.btnTimes.clicked.connect(self.mulButton)
		self.btnDivide.clicked.connect(self.divButton)

		self.btnEquals.clicked.connect(self.equalButton)

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

		self.firstNum = ""
		self.thereOperation = False
		self.symbol = ""



	def allClear(self):
		self.lcdAnswer.display(0)
		self.firstNum = ""
		self.thereOperation = 0
		self.symbol = ""
		print(self.thereOperation)
		print(self.firstNum)
		print(self.symbol)

	def clear(self):
		pat = re.compile(self.ONE_NUMBER)
		num = str(int(self.lcdAnswer.value()))
		if pat.match(num):
			self.allClear()
		else:
			tex = num[:-1]
			self.lcdAnswer.display(str(tex))



	def isZero(self):
		return self.lcdAnswer.value() == 0

	def isFull(self):
		pat = re.compile(self.EIGHT_NUMBERS)
		num = str(int(self.lcdAnswer.value()))
		return pat.match(num)



	def addButton(self):
		print(self.symbol)
		self.firstNum = int(self.lcdAnswer.value())
		self.thereOperation = True
		self.symbol = "+"
		print(self.symbol)

	def subButton(self):
		print(self.symbol)
		self.firstNum = int(self.lcdAnswer.value())
		self.thereOperation = True
		self.symbol = "-"
		print(self.symbol)

	def mulButton(self):
		print(self.symbol)
		self.firstNum = int(self.lcdAnswer.value())
		self.thereOperation = True
		self.symbol = "*"
		print(self.symbol)

	def divButton(self):
		print(self.symbol)
		self.firstNum = int(self.lcdAnswer.value())
		self.thereOperation = True
		self.symbol = "/"
		print(self.symbol)

	def equalButton(self):
		print(self.symbol)
		if not self.firstNum == "":
			if self.symbol == "+":
				ans = self.firstNum + int(self.lcdAnswer.value())
			if self.symbol == "-":
				ans = self.firstNum - int(self.lcdAnswer.value())
			if self.symbol == "*":
				ans = self.firstNum * int(self.lcdAnswer.value())
			if self.symbol == "/":
				ans = self.firstNum / int(self.lcdAnswer.value())
			print(ans)
			self.lcdAnswer.display(int(ans))
			print(self.symbol)



	def addNum0(self):
		if not self.isFull():
			if not self.isZero() or not self.thereOperation:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'0')

	def addNum1(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(1)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'1')

	def addNum2(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(2)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'2')

	def addNum3(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(3)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'3')

	def addNum4(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(4)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'4')

	def addNum5(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(5)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'5')

	def addNum6(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(6)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'6')

	def addNum7(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(7)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'7')

	def addNum8(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(8)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'8')

	def addNum9(self):
		if not self.isFull():
			if self.isZero() or self.thereOperation:
				self.lcdAnswer.display(9)
				self.thereOperation = False
			else:
				v = str(int(self.lcdAnswer.value()))
				self.lcdAnswer.display(v+'9')

app = QApplication(sys.argv)
window = MainView()
window.show()
app.exec_()