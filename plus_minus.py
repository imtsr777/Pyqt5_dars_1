from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QTextEdit

from PyQt5.QtGui import QIcon

import sys

class MainWindow( QMainWindow ):
    _counter = 0

    def __init__(self):
        super().__init__()
        self.windowSettings()

    def windowSettings(self):
        self.setFixedSize(300, 500)
        self.btnPlus = QPushButton("+", self)
        self.btnPlus.setGeometry(40, 50, 60, 60)

        self.btnMinus = QPushButton("-", self)
        self.btnMinus.setGeometry(190, 50, 60, 60)

        self.point = QLabel("0", self)
        self.point.move(140, 50)
        self.point.setStyleSheet("font-size: 30px")

        self.btnMinus.clicked.connect(self.decreasing)
        self.btnPlus.clicked.connect(self.increasing)

        self.lineEdit1 = QLineEdit(self)

        self.btn = QPushButton("Click",self)
        self.btn.clicked.connect(self.showLineEditText)
        self.btn.move(130, 0)


    def increasing(self):
        self.lineEdit1.setText("O'syapti")
        self._counter += 1
        self.point.setText(f"{self._counter}")

    def decreasing(self):
        self.lineEdit1.setText("Kamayapti")

        if( self._counter > 0 ):
            self._counter -= 1

        self.point.setText(f"{self._counter}")


    def showLineEditText(self):
        
        print(self.lineEdit1.text())





app = QApplication([])
print(sys.argv)
window = MainWindow()
window.show()
app.exec()