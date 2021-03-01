from gen.add_stock_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from datetime import date as dt
import investpy
import yfinance
import pandas
from datetime import date
from add_trans import currencies

# Do not change the order in sTypes! You can append types to the end
sTypes = ["Stock", "ETF", "Fund", "Crypto"]

methods = ["yfinance", "investpy"] 

# Works only with a correct ticker
def get_price_yfinance(sticker):
    ticker = yfinance.Ticker(sticker)
    try:
        price = ticker.history(period="today").iloc[-1]['Close']
        return price
    except Exception as e:
        raise MethodNotWorkingError
    

def get_price_investpy(sname, sticker, stype, scountry):
    if stype == "Stock":
        try:
            df = investpy.get_stock_recent_data(sname, scountry)
        except RuntimeError:
            try:
                df = investpy.get_stock_recent_data(sticker, scountry)
            except RuntimeError:
                raise MethodNotWorkingError
    elif stype == "Fund":
        try:
            df = investpy.get_fund_recent_data(sname, scountry)
        except RuntimeError:
            try:
                df = investpy.get_fund_recent_data(sticker, scountry)
            except RuntimeError:
                raise MethodNotWorkingError
    elif stype == "ETF":
        try:
            df = investpy.get_etf_recent_data(sname, scountry)
        except RuntimeError:
            try:
                df = investpy.get_etf_recent_data(sticker, scountry)
            except RuntimeError:
                raise MethodNotWorkingError
    elif stype == "Crypto":
        try:
            df = investpy.get_crypto_recent_data(sname)
        except RuntimeError:
            try:
                df = investpy.get_crypto_recent_data(sticker)
            except RuntimeError:
                raise MethodNotWorkingError
    else:
        raise MethodNotWorkingError

    return df.iloc[-1]['Close']



class MethodNotWorkingError(Exception):
    # Raised when method cannot fetch price data
    pass

class InvalidValueError(Exception):
    # Raised when the value inserted is erronous
    pass

class Stock(QObject):

    erronous = pyqtSignal(str)

    def __init__(self, sname, sticker, scountry, stype, smethod, scurrency):
        super().__init__()
        self.sname = sname
        self.sticker = sticker
        self.scountry = scountry
        self.stype = stype
        self.smethod = smethod
        self.scurrency = scurrency

    def compose_sql(self):
        try:
            num_of_values = 6
            sql_msg = "INSERT INTO stocks VALUES ("
            sql_msg += "DEFAULT, "
            for i in range(0, num_of_values - 1):
                sql_msg += "'{}', "
            sql_msg += "'{}')"
            sql_msg = sql_msg.format(self.sname, self.sticker, self.scountry, 
                                     self.stype, self.smethod, self.scurrency)
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
            self.scurrency = self.verify_scurrency(self.scurrency)
            print(self.stype)
            if self.smethod == "investpy":
                testprice = get_price_investpy(self.sname, self.sticker, 
                                                self.stype, self.scountry)
                return True
            elif self.smethod == 'yfinance':
                testprice = get_price_yfinance(self.sticker)
                return True
            self.erronous.emit("Method not implemented yet")
            return False
        except InvalidValueError:
            return False
        except ValueError:
            self.erronous.emit("Did you leave some fields blank?")
            return False
        except MethodNotWorkingError:
            self.erronous.emit("Method not working")
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

    # All types but cryptos need to specify their country for investpy
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

    def verify_scurrency(self, scurrency):
        if not scurrency in currencies:
            self.erronous.emit("Currency not supported")
            raise InvalidValueError
        else:
            return scurrency

class AddStockForm(QtWidgets.QWidget):

    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_stock)
        self.ui.pushButton_test.clicked.connect(self.test_method)
        self.stockdb = db
        self.ui.combo_sType.addItems(sTypes)
        self.ui.combo_sMethod.addItems(methods)
        self.ui.combo_sCurrency.addItems(currencies)

    def add_stock(self):
        stock = Stock(
            self.ui.line_sName.text(),
            self.ui.line_sTicker.text(),
            self.ui.line_scountry.text(),
            self.ui.combo_sType.currentText(),
            self.ui.combo_sMethod.currentText(),
            self.ui.combo_sCurrency.currentText()
        )

        stock.erronous.connect(self.errorprinter)
        sql_msg = self.stockdb.stocks.select_tickers(stype=self.ui.combo_sType.currentText())
        tickers_in_db = [item for t in self.stockdb.query(sql_msg) for item in t]

        if self.ui.line_sTicker.text() in tickers_in_db:
            self.errorprinter("Ticker already in use!")

        elif stock.verify():
            sql_msg = stock.compose_sql()
            print(sql_msg)
            self.stockdb.insert(sql_msg)

    def test_method(self):
        if self.ui.combo_sMethod.currentText() == "investpy":
            try:
                sprice = get_price_investpy(self.ui.line_sName.text(),
                                            self.ui.line_sTicker.text(),
                                            self.ui.combo_sType.currentText(),
                                            self.ui.line_scountry.text())
                self.ui.label_test.setText(str(sprice))
            except MethodNotWorkingError:
                self.errorprinter("Method not working")
        elif self.ui.combo_sMethod.currentText() == "yfinance":
            try:
                sprice = get_price_yfinance(self.ui.line_sTicker.text())
                self.ui.label_test.setText(str(sprice))
            except MethodNotWorkingError:
                self.errorprinter("Method not working")
        else:
            self.errorprinter("Method not yet implemented")


    def errorprinter(self, er_msg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Error adding value")
        msg.setInformativeText(er_msg)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()