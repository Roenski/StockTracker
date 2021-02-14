from PyQt5 import QtCore, QtGui, QtWidgets
from menu_win import Ui_Form

class Menu(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
