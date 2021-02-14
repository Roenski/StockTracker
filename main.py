from PyQt5 import QtCore, QtGui, QtWidgets 
from mw import Ui_MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.pushButton3.clicked.connect(MainWindow.close)
    ui.actionExit.triggered.connect(MainWindow.close)

    MainWindow.show()
    sys.exit(app.exec_())

