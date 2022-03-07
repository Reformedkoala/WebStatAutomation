from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class GUIWindows(QMainWindow):
    def __init__(self):
        super(GUIWindows, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Example GUI")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Graphic Design is my Passion")
        self.label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.update()

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click this")
        #self.button.setAlignment(QtCore.Qt.AlignCenter)
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Graphic Design is still my passion")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = GUIWindows()

    win.show()
    sys.exit(app.exec_())

window()