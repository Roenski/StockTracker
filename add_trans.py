from add_trans_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets

class AddTransactionForm(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
