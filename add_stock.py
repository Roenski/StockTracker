from gen.add_stock_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from datetime import date as dt

sTypes = ["Stock", "ETF", "Fund", "Crypto"]
methods = ["yfinance", "investpy"] 

class AddStockForm(QtWidgets.QWidget):

    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stockdb = db
        self.ui.combo_sType.addItems(sTypes)
        self.ui.combo_sMethod.addItems(methods)