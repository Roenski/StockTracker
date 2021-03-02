from PyQt5 import QtCore, QtGui, QtWidgets 
from gen.main_win import Ui_MainWindow
from menu import Menu
from add_trans import AddTransactionForm
from list_trans import ListTransactionForm
from list_stock import ListStockForm
from add_stock import AddStockForm
from db import Database
class MainWin(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.main_menu = Menu()
        self.database = Database("stocktracker", "db.ini", self.ui.statusbar.showMessage)
        self.database.connect_db()
        self.database.close()
        self.add_trans = AddTransactionForm(self.database)
        self.add_stock = AddStockForm(self.database) 
        self.list_trans = ListTransactionForm(self.database)
        self.list_stocks = ListStockForm(self.database) 
        self.central_widget.addWidget(self.main_menu)
        self.central_widget.addWidget(self.add_trans)
        self.central_widget.addWidget(self.add_stock)
        self.central_widget.addWidget(self.list_trans)
        self.central_widget.addWidget(self.list_stocks)

        self.ui.actionExit.triggered.connect(self.close)
        self.main_menu.exited.connect(self.close)
        self.main_menu.ui.button_add_transaction.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.add_trans))
        self.main_menu.ui.button_list_transactions.clicked.connect \
            (self.list_trans_event)
        self.main_menu.ui.button_list_stocks.clicked.connect \
            (self.list_stock_event)
        self.main_menu.ui.button_add_stock.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.add_stock))
        self.add_trans.ui.pushButton_cancel.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.main_menu))
        self.list_trans.ui.return_btn.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.main_menu))
        self.add_stock.ui.pushButton_cancel.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.main_menu))
        self.list_stocks.ui.return_btn.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.main_menu))
        self.central_widget.setCurrentWidget(self.main_menu)

        self.resize(1400,600)

    def list_trans_event(self):
        self.list_trans.load_entries()
        self.central_widget.setCurrentWidget(self.list_trans)

    def list_stock_event(self):
        self.list_stocks.load_entries()
        self.central_widget.setCurrentWidget(self.list_stocks)

    def closeEvent(self, event):
        self.database.close()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

#    # Set up the main window
    MainWindow = MainWin()
    MainWindow.show()
    sys.exit(app.exec_())

