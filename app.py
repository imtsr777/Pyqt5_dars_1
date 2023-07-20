from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

import sys

class MainWindow( QMainWindow ):

    def __init__(self):
        super().__init__()

        # self.setFixedSize(400,400) # Fix o'lcham
        # self.setMinimumSize(400,400)
        # self.setMaximumSize(700, 700)
        # self.setFixedHeight(600)
        # self.setFixedWidth(500)
        # self.setWindowTitle("Salom")
        # self.setBaseSize(800, 800)
        # self.setStyleSheet('background-color: black;')
        # self.setWindowIcon(QIcon("IMG_1258.jpg"))
        




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()