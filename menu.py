from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from menu_win import Ui_Form

class Menu(QtWidgets.QWidget):

    exited = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_exit.clicked.connect(self.exited.emit)
