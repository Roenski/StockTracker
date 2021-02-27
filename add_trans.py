from gen.add_trans_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from datetime import date as dt

# These should probably come from a file in the future
ttypes = ["Stock", "ETF", "Fund", "Crypto"]
tBSs = ["Buy", "Sell"]
sNames = ["Test", "AMD", "OTE1V", "SXR8", "DIS", "EUNK"] # Make a database for these!
currencies = ["USD", "EUR", "SEK", "CAD"]
tBrokers = ["Nordnet", "OP", "Degiro", "Coinmotion"]

class InvalidValueError(Exception):
    # Raised when the value inserted is erronous
    pass

class Transaction(QObject):

    erronous = pyqtSignal(str)

    def __init__(self, tdate, ttype, tbs, sname, 
                squantity, sprice, spricecurrency, spriceexchange, 
                sfee, sfeecurrency, sfeeexchange, tbroker):
        super().__init__()
        self.tdate = tdate
        self.ttype = ttype
        self.tbs = tbs
        self.sname = sname
        self.squantity = squantity
        self.sprice = sprice
        self.spricecurrency = spricecurrency
        self.spriceexchange = spriceexchange
        self.sfee = sfee
        self.sfeecurrency = sfeecurrency
        self.sfeeexchange = sfeeexchange
        self.tbroker = tbroker

    # Run this after a successful run of self.verify
    def compose_sql(self):
        try:
            num_of_values = 12
            sql_msg =   "INSERT INTO transactions VALUES ("
            sql_msg += "DEFAULT, " 
            for i in range(0, num_of_values - 1):
                sql_msg += "'{}', "
            sql_msg += "'{}')"
            sql_msg = sql_msg.format(self.tdate, self.ttype, self.tbs, self.sname,
                                    self.squantity, self.sprice, self.spricecurrency,
                                    self.spriceexchange, self.sfee, self.sfeecurrency,
                                    self.sfeeexchange, self.tbroker)
            return sql_msg
        except Exception as e:
            self.erronous.emit("Something went wrong.")
            print(e)
            return ""
            
    
    def verify(self):
        try:
            self.tdate = self.verify_tdate(self.tdate)
            self.ttype = self.verify_ttype(self.ttype)
            self.tbs = self.verify_tbs(self.tbs)
            self.sname = self.verify_sname(self.sname)
            self.squantity = self.verify_squantity(self.squantity)
            self.sprice = self.verify_sprice(self.sprice)
            self.spricecurrency = self.verify_spricecurrency(self.spricecurrency)
            self.spriceexchange = self.verify_spriceexchange(self.spriceexchange)
            self.sfee = self.verify_sfee(self.sfee)
            self.sfeecurrency = self.verify_sfeecurrency(self.sfeecurrency)
            self.sfeeexchange = self.verify_sfeeexchange(self.sfeeexchange)
            self.tbroker = self.verify_tbroker(self.tbroker)
            return True
        except InvalidValueError:
            # When this happens, an error message is generated
            # already in the verify-function
            return False
        except ValueError:
            self.erronous.emit("Did you leave some fields blank?")
            return False
        
    def verify_tdate(self, tdate):
        date = tdate.date()
        today = dt.today()
        if   date.year() >  today.year or \
            (date.year() == today.year and date.month() > today.month) or \
            (date.year() == today.year and date.month() == today.month and date.day() > today.day):
            self.erronous.emit("Date cannot be in the future!")
            raise InvalidValueError
        else:
            return "{}/{}/{}".format(date.year(), date.month(), date.day())
    def verify_ttype(self, ttype):
        if not ttype in ttypes:
            self.erronous.emit("Wrong type of commodity")
            raise InvalidValueError
        else:
            return ttype
    def verify_tbs(self, tbs):
        if not tbs in tBSs:
            self.erronous.emit("Wrong type of transaction")
            raise InvalidValueError
        else:
            return tbs
    def verify_sname(self, sname):
        if not sname in sNames:
            self.erronous.emit("Stock not added to the list")
            raise InvalidValueError
        else:
            return sname
    def verify_squantity(self, squantity):
        if float(squantity) <= 0:
            self.erronous.emit("Stock quantity cannot be under 0. Use sell-type for sales.")
            raise InvalidValueError
        else:
            return squantity
    def verify_sprice(self, sprice):
        if float(sprice) <= 0:
            self.erronous.emit("Stock price cannot be equal or less than 0")
            raise InvalidValueError
        else:
            return sprice
    def verify_spricecurrency(self, spricecurrency):
        if not spricecurrency in currencies:
            self.erronous.emit("Price currency not added to the list")
            raise InvalidValueError
        else:
            return spricecurrency
    def verify_spriceexchange(self, spriceexchange):
        if float(spriceexchange) <= 0:
            self.erronous.emit("Exchange rate cannot be negative or zero")
            raise InvalidValueError
        else:
            return spriceexchange
    def verify_sfee(self, sfee):
        if float(sfee) < 0:
            self.erronous.emit("Fee cannot be negative")
            raise InvalidValueError
        else:
            return sfee 
    def verify_sfeecurrency(self, sfeecurrency):
        if not sfeecurrency in currencies:
            self.erronous.emit("Fee currency not added to the list")
            raise InvalidValueError
        else:
            return sfeecurrency
    def verify_sfeeexchange(self, sfeeexchange):
        if float(sfeeexchange) <= 0:
            self.erronous.emit("Exchange rate cannot be negative or zero.")
            raise InvalidValueError
        else:
            return sfeeexchange
    def verify_tbroker(self, tbroker):
        if not tbroker in tBrokers:
            self.erronous.emit("Broker not added to the list")
            raise InvalidValueError
        else:
            return tbroker

class AddTransactionForm(QtWidgets.QWidget):

    def __init__(self, db):
        super().__init__()
        # Database to add transactions to
        self.db = db
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_transaction)
        self.ui.combo_tType.addItems(ttypes)
        self.ui.combo_tBS.addItems(tBSs)
        self.ui.combo_sName.addItems(sNames)
        self.ui.combo_sPriceCurrency.addItems(currencies)
        self.ui.combo_sFeeCurrency.addItems(currencies)
        self.ui.combo_tBroker.addItems(tBrokers)
        
    def add_transaction(self):
        # order is very important here (verify last!)
        trans = Transaction(
            self.ui.edit_tDate,
            self.ui.combo_tType.currentText(),
            self.ui.combo_tBS.currentText(),
            self.ui.combo_sName.currentText(),
            self.ui.line_sQuantity.text(),
            self.ui.line_sPrice.text(),
            self.ui.combo_sPriceCurrency.currentText(),
            self.ui.line_sPriceExchange.text(),
            self.ui.line_sFee.text(),
            self.ui.combo_sFeeCurrency.currentText(),
            self.ui.line_sFeeExchange.text(),
            self.ui.combo_tBroker.currentText()
        )
        # In the case of an error, the error message is sent
        # via a pyqt signal
        trans.erronous.connect(self.errorprinter)
        
        if trans.verify():
            sql_msg = trans.compose_sql()
            self.db.insert(sql_msg)
            print(sql_msg)

    def errorprinter(self, er_msg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Error adding value")
        msg.setInformativeText(er_msg)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


