from PyQt5 import QtCore, QtGui, QtWidgets 
from main_win import Ui_MainWindow
from menu import Menu
from add_trans import AddTransactionForm
from db import Database

class MainWin(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main_menu = Menu()
        self.add_trans = AddTransactionForm()

        self.ui.actionExit.triggered.connect(self.close)
        #self.main_menu.clicked.connect(self.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
#
#    # Set up the main window
    MainWindow = MainWin()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#
#    # Set up the main menu -widget
#    main_menu = Menu()
#
#    # Set up the add transaction -widget
#    add_trans = AddTransactionForm()
#
#    # Set up exit buttons
#    ui.actionExit.triggered.connect(MainWindow.close)
#    main_menu.ui.button_exit.clicked.connect(MainWindow.close)
#
#    # Set up rest of the buttons
#    main_menu.ui.button_add_transaction.clicked.connect(lambda: MainWindow.setCentralWidget(add_trans))
#    add_trans.ui.pushButton_cancel.clicked.connect(lambda: MainWindow.setCentralWidget(main_menu))
#
#    # Set the main window as central widget
#    MainWindow.setCentralWidget(main_menu)
#
#    database = Database('db.ini')
#    database.connect(ui.statusbar.showMessage)
#
#
    MainWindow.show()
    sys.exit(app.exec_())

