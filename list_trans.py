from gen.list_trans_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt


class ListTransactionForm(QtWidgets.QWidget):
    def __init__(self, database):
        super().__init__()
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.db = database
        self.list = ListTransactionTable()
        self.ui.list_tbl.setModel(self.list)

    def load_entries(self):
        entries = self.db.select_all(10)
        #self.list.data = entries
        print(entries)

class ListTransactionTable(QtCore.QAbstractTableModel):

    def __init__(self):
        super().__init__()
        self._data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
          [7, 8, 9],
        ] 
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

        ##self.ui.transList.