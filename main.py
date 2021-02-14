from PyQt5 import QtCore, QtGui, QtWidgets 
from main_win import Ui_MainWindow
from menu import Menu
from add_trans import AddTransactionForm
from db import Database

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Set up the main window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Set up the main menu -widget
    main_menu = Menu()

    # Set up the add transaction -widget
    add_trans = AddTransactionForm()

    # Set up exit buttons
    ui.actionExit.triggered.connect(MainWindow.close)
    main_menu.ui.button_exit.clicked.connect(MainWindow.close)

    # Set up rest of the buttons
    main_menu.ui.button_add_transaction.clicked.connect(lambda: MainWindow.setCentralWidget(add_trans))

    # Set the main window as central widget
    MainWindow.setCentralWidget(main_menu)

    database = Database('db.ini')
    database.connect(ui.statusbar.showMessage)


    MainWindow.show()
    sys.exit(app.exec_())

