from gen.list_trans_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QMessageBox

ENTRIES_PER_PAGE = 10
NO_OF_COLUMNS = 13

class ListTransactionForm(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.db = db

        self.list_trans = None
        self.page = 0
        self.MAX_PAGE = False

        self.ui.next_btn.clicked.connect(self.next_page)
        self.ui.prev_btn.clicked.connect(self.prev_page)
        self.ui.delete_btn.clicked.connect(self.delete_entry)
        
        self.ui.list_tbl.resizeRowToContents(2)

    def load_entries(self):
        sql_msg = self.db.transactions.select_all(ENTRIES_PER_PAGE, self.page*ENTRIES_PER_PAGE)
        entries = self.db.query(sql_msg)
        self.list_trans = ListTransactionTable(entries)
        self.ui.list_tbl.setModel(self.list_trans)
        if len(entries) < ENTRIES_PER_PAGE:
            self.MAX_PAGE = True
        else:
            self.MAX_PAGE = False

    def delete_entry(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        # this snippet gets the tid of the current selection
        row = self.ui.list_tbl.model().index(self.ui.list_tbl.currentIndex().row(),0)
        print(row.row())
        print(row.data())

        msg.setText("Are you sure you want to delete this entry?")
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel)
        #msg.buttonClicked.connect(self.delete_confirm)
        answer = msg.exec_()
        if answer == QMessageBox.Yes:
            self.db.delete_entry(row.data())
            self.load_entries()

    def next_page(self):
        if not self.MAX_PAGE:
            self.page += 1
            self.load_entries()

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.load_entries()

class ListTransactionTable(QtCore.QAbstractTableModel):

    def __init__(self, data_init):
        super().__init__()
        self._data = self.parse_data(data_init)
        self._headers = ["Transation ID", "Date", "Type", "Buy/Sell",
                            "Stock Name", "Quantity", "Price",
                            "Currency", "Exchange Rate", "Fee",
                            "Fee Currency", "Exchange Rate", "Broker"]
        
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
            entry[1] = str(entry[1])
            entry[5] = str(entry[5])
            entry[6] = str(entry[6])
            entry[8] = str(entry[8])
            entry[9] = str(entry[9])
            entry[11] = str(entry[11])
            data_p.append(entry)
        return data_p

