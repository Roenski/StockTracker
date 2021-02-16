from add_trans_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets

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
        print(tdate)
        return 0
    def verify_ttype(self, ttype):
        print(ttype)
        return 0
    def verify_tbs(self, tbs):
        print(tbs)
        return 0
    def verify_sname(self, sname):
        print(sname)
        return 0
    def verify_squantity(self, squantity):
        print(squantity)
        return 0
    def verify_sprice(self, sprice):
        print(sprice)
        return 0
    def verify_spricecurrency(self, spricecurrency):
        print(spricecurrency)
        return 0
    def verify_spriceexchange(self, spriceexchange):
        print(spriceexchange)
        return 0
    def verify_sfee(self, sfee):
        print(sfee)
        return 0
    def verify_sfeecurrency(self, sfeecurrency):
        print(sfeecurrency)
        return 0
    def verify_sfeeexchange(self, sfeeexchange):
        print(sfeeexchange)
        return 0
    def verify_tbroker(self, tbroker):
        print(tbroker)
        return 0

class AddTransactionForm(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_transaction)
        
    def add_transaction(self):
        trans = Transaction(
            self.ui.edit_tDate.text(),
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

