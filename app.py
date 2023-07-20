from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QTextEdit

from PyQt5.QtGui import QIcon

import sys

class MainWindow( QMainWindow ):

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

        # self.btn1 = QPushButton(self)
        # self.btn1.setText("Button")
        # self.btn1.setText("Knopka")


app = QApplication([])
print(sys.argv)
window = MainWindow()
window.show()
app.exec()