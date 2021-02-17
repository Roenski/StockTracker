from add_trans_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date as dt

# These should probably come from a file in the future
ttypes = ["Stock", "ETF", "Fund", "Crypto"]
tBSs = ["Buy", "Sell"]
sNames = ["AMD", "OTE1V", "SXR8", "DIS", "EUNK"] # Make a database for these!
currencies = ["USD", "EUR", "SEK"]
tBrokers = ["Nordnet", "OP", "Degiro", "Coinmotion"]

class Transaction:

    def __init__(self, tdate, ttype, tbs, sname, 
                squantity, sprice, spricecurrency, spriceexchange, 
                sfee, sfeecurrency, sfeeexchange, tbroker):
        #self.tid = self.verify_tid(tid)
        self.tdate = self.verify_tdate(tdate)
        self.ttype = self.verify_ttype(ttype)
        self.tbs = self.verify_tbs(tbs)
        self.sname = self.verify_sname(sname)
        self.squantity = self.verify_squantity(squantity)
        self.sprice = self.verify_sprice(sprice)
        self.spricecurrency = self.verify_spricecurrency(spricecurrency)
        self.spriceexchange = self.verify_spriceexchange(spriceexchange)
        self.sfee = self.verify_sfee(sfee)
        self.sfeecurrency = self.verify_sfeecurrency(sfeecurrency)
        self.sfeeexchange = self.verify_sfeeexchange(sfeeexchange)
        self.tbroker = self.verify_tbroker(tbroker)
        
    def verify_tid(self, tid):
        print(tid)
        return 0
    def verify_tdate(self, tdate):
        date = tdate.date()
        today = dt.today()
        if   date.year() >  today.year or \
            (date.year() == today.year and date.month() > today.month) or \
            (date.year() == today.year and date.month() == today.month and date.day() > today.day):
            print("Date cannot be in the future!")
        return 0
    def verify_ttype(self, ttype):
        if not ttype in ttypes:
            print("Wrong type of commodity")
        return 0
    def verify_tbs(self, tbs):
        if not tbs in tBSs:
            print("Wrong type of transaction")
        return 0
    def verify_sname(self, sname):
        if not sname in sNames:
            print("Stock not added to the list")
        return 0
    def verify_squantity(self, squantity):
        if float(squantity) <= 0:
            print("Stock quantity cannot be under 0. Use sell-type for sales.")
        return 0
    def verify_sprice(self, sprice):
        if float(sprice) <= 0:
            print("Stock price cannot be equal or less than 0")
        return 0
    def verify_spricecurrency(self, spricecurrency):
        if not spricecurrency in currencies:
            print("Price currency not added to the list")
        return 0
    def verify_spriceexchange(self, spriceexchange):
        if float(spriceexchange) <= 0:
            print("Exchange rate cannot be negative or zero")
        return 0
    def verify_sfee(self, sfee):
        if float(sfee) < 0:
            print("Fee cannot be negative")
        return 0
    def verify_sfeecurrency(self, sfeecurrency):
        if not sfeecurrency in currencies:
            print("Fee currency not added to the list")
        return 0
    def verify_sfeeexchange(self, sfeeexchange):
        if float(sfeeexchange) <= 0:
            print("Exchange rate cannot be negative or zero.")
        return 0
    def verify_tbroker(self, tbroker):
        if not tbroker in tBrokers:
            print("Broker not added to the list")
        return 0

class AddTransactionForm(QtWidgets.QWidget):



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

