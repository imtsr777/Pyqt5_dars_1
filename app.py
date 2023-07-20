from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QTextEdit

from PyQt5.QtGui import QIcon

import sys

class MainWindow( QMainWindow ):
    _counter = 0
    _raise = True
    _clicksCount = 0;
    def __init__(self):
        super().__init__()

        self.setFixedSize(400,400) # Fix o'lcham
        # self.setMinimumSize(400,400)
        # self.setMaximumSize(700, 700)
        # self.setFixedHeight(600)
        # self.setFixedWidth(500)
        # self.setWindowTitle("Salom")
        # self.setBaseSize(800, 800)
        # self.setStyleSheet('background-color: black;')
        # self.setWindowIcon(QIcon("IMG_1258.jpg"))

# "================================================================="

        # self.text1 = QLabel("Salom", self)
        # # self.text1.setGeometry(30, 70, 200, 70)
        # self.text1.setStyleSheet("font-size: 40px;");
        # self.text1.adjustSize()

        # self.text2 = QLabel("Hello", self)
        # self.text2.move(30, 70)
        # self.text2.setStyleSheet("font-size: 40px;")
        # self.text2.adjustSize()

# "================================================================="
        # self.lineEdit1 = QLineEdit(self)
        # self.setStyleSheet("""
        #                    font-size: 30px;
        #                    font-family: Times new Roman
        #                    """)

# "================================================================="

        # self.bigText = QTextEdit(self)
        # self.bigText.setFixedSize(200, 200)

# "================================================================="

        self.btn1 = QPushButton(self)
        self.btn1.setText("Button")
        self.btn1.clicked.connect(self.buttonClicked)

        self.labelNumber = QLabel("0",self)
        self.labelNumber.move(40, 40)
        self.labelNumber.setStyleSheet("font-size: 30px")

        self.labelCount = QLabel("0",self)
        self.labelCount.move(70, 40)
        self.labelCount.setStyleSheet("font-size: 30px; color: red;")

    def buttonClicked(self):
        
        self._clicksCount += 1
        self.labelCount.setText(f"{self._clicksCount}")

        if( self._raise ):
            self._counter += 1
        else:
            self._counter -= 1

        if( self._counter == 10 ):
            self._raise = False
        elif( self._counter == 0 ):
            self._raise = True

        self.labelNumber.setText(f"{self._counter}")



app = QApplication([])
print(sys.argv)
window = MainWindow()
window.show()
app.exec()