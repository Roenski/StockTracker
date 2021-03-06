from gen.distribution_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QMessageBox
from add_trans import ttypes

class DistributionForm(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.db = db

        sql_msg = self.load_type("ETF")
        entries = self.db.query(sql_msg)
        print(entries)

    def load_type(self, stype):
        sql_msg = self.db.transactions.select_by_type(stype)
        return sql_msg

class DistributionTable(QtCore.QAbstractTableModel):

    def __init__(self, data_init):
        super().__init__()
        self._data = self.parse_data(data_init)
        self._headers = ["ETF+Fund", "ETF+Fund current", "Stock", "Stock current",
                                 "Crypto", "Crypto current"]

        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._headers[section]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def parse_data(self, data_up):
        data_p = []
        for i in range(0, len(data_up)):
            entry = list(data_up[i])
            data_p.append(entry[0:])
        return data_p

