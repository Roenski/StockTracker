from gen.list_trans_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

class ListTransactionForm(QtWidgets.QWidget):

    def __init__(self, database):
        super().__init__()
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.db = database

        ##self.ui.transList.