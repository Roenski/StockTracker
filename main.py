from PyQt5 import QtCore, QtGui, QtWidgets 
from gen.main_win import Ui_MainWindow
from menu import Menu
from add_trans import AddTransactionForm
from list_trans import ListTransactionForm
from db import TransactionDB

class MainWin(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.main_menu = Menu()
        self.database = TransactionDB('db.ini', self.ui.statusbar.showMessage)
        self.database.connect_db()
        self.add_trans = AddTransactionForm(self.database)
        self.list_trans = ListTransactionForm(self.database)
        self.central_widget.addWidget(self.main_menu)
        self.central_widget.addWidget(self.add_trans)
        self.central_widget.addWidget(self.list_trans)
        self.ui.actionExit.triggered.connect(self.close)
        self.main_menu.exited.connect(self.close)
        self.main_menu.ui.button_add_transaction.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.add_trans))
        self.main_menu.ui.button_list_transactions.clicked.connect(self.list_view_event)
        self.add_trans.ui.pushButton_cancel.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.main_menu))
        self.list_trans.ui.return_btn.clicked.connect \
            (lambda: self.central_widget.setCurrentWidget(self.main_menu))
        self.central_widget.setCurrentWidget(self.main_menu)

        self.resize(1400,600)

    def list_view_event(self):
        self.list_trans.load_entries()
        self.central_widget.setCurrentWidget(self.list_trans)

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

