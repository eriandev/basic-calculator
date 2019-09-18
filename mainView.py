
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("calculator.ui", self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Basic Calculator")
        
        self.lcdAnswer.display("Error404")

app = QApplication(sys.argv)
window = MainView()
window.show()
app.exec_()