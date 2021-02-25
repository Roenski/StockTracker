from gen.add_stock_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from datetime import date as dt
import investpy

sTypes = ["Stock", "ETF", "Fund", "Crypto"]
methods = ["yfinance", "investpy"] 

def get_price_investpy(name, ticker, country):
    pass

class InvalidValueError(Exception):
    # Raised when the value inserted is erronous
    pass

class Stock(QObject):

    erronous = pyqtSignal(str)

    def __init__(self, sname, sticker, scountry, stype, smethod):
        super().__init__()
        self.sname = sname
        self.sticker = sticker
        self.scountry = scountry
        self.stype = stype
        self.smethod = smethod

    def compose_sql(self):
        try:
            num_of_values = 5
            sql_msg = "INSERT INTO stocks VALUES ("
            sql_msg += "DEFAULT, "
            for i in range(0, num_of_values - 1):
                sql_msg += "'{}, "
            sql_msg += "'{}')"
            sql_msg += sql_msg.format(self.sname, self.sticker, self.scountry, 
                                     self.stype, self.smethod)
            return sql_msg
        except Exception as e:
            self.erronous.emit("Something went wrong.")
            print(e)
            return ""

    def verify(self):
        try:
            self.sname = self.verify_sname(self.sname)
            self.sticker = self.verify_sticker(self.sticker)
            self.scountry = self.verify_scountry(self.scountry, self.stype)
            self.stype = self.verify_stype(self.stype)
            self.smethod = self.verify_smethod(self.smethod)
            return True
        except InvalidValueError:
            return False
        except ValueError:
            self.erronous.emit("Did you leave some fields blank?")
            return False


    def verify_sname(self, sname):
        if sname == "":
            self.erronous.emit("Stock name is blank!")
            raise InvalidValueError
        else:
            return sname

    def verify_sticker(self, sticker):
        if sticker == "":
            self.erronous.emit("Stock ticker is blank!")
            raise InvalidValueError
        else:
            return sticker

    def verify_scountry(self, scountry, stype):
        if scountry == "" and stype in sTypes[0:3]:
            self.erronous.emit("Stock country is blank!")
            raise InvalidValueError
        else:
            return scountry

    def verify_stype(self, stype):
        if not stype in sTypes:
            self.erronous.emit("Invalid type of stock")
            raise InvalidValueError
        else:
            return stype

    def verify_smethod(self, smethod):
        if not smethod in methods:
            self.erronous.emit("Invalid method")
            raise InvalidValueError
        else:
            return smethod

class AddStockForm(QtWidgets.QWidget):

    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_stock)
        self.stockdb = db
        self.ui.combo_sType.addItems(sTypes)
        self.ui.combo_sMethod.addItems(methods)

    def add_stock(self):
        stock = Stock(
            self.ui.line_sName.text(),
            self.ui.line_sTicker.text(),
            self.ui.line_scountry.text(),
            self.ui.combo_sType.currentText(),
            self.ui.combo_sMethod.currentText()
        )

        stock.erronous.connect(self.errorprinter)

        if stock.verify():
            print(stock.compose_sql())

    def errorprinter(self, er_msg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Error adding value")
        msg.setInformativeText(er_msg)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()