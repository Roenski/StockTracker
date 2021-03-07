from gen.distribution_win import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QMessageBox
from add_trans import ttypes
from add_stock import get_price_investpy, get_price_yfinance
from decimal import *
import datetime


# Calculates gains using FIFO principle
def calculate_gains(db, stype):
    if stype in ttypes:
        # Get all different tickers in this type
        # This method automatically orders the transactions by date
        sql_msg = db.transactions.select_names_by_type(stype)
        names = db.query(sql_msg)
        gains = 0
        for name in names:
            name = name[0]
            sql_msg = db.transactions.select_by_bs_type_name("Buy", stype, name)
            buy_entries = db.query(sql_msg)
            sql_msg = db.transactions.select_by_bs_type_name("Sell", stype, name)
            sell_entries = db.query(sql_msg)
            # Create a mutable list for buys and sells
            buys = []
            sells = []
            for buy in buy_entries:
                print(buy[1])
                entry = []
                entry.append(buy[5]) 
                # Total unit price in euros
                # Unit_price*exchange_rate + fee*exchange_rate/quantity
                entry.append(buy[6]*buy[8] + buy[9]*buy[11]/buy[5]) 
                buys.append(entry)
            for sell in sell_entries:
                entry = []
                # Quantity
                entry.append(sell[5]) 
                # Total unit price in euros
                # Unit_price*exchange_rate - fee*exchange_rate/quantity
                entry.append(sell[6]*sell[8] - sell[9]*sell[11]/sell[5]) 
                sells.append(entry)

            # Calculate gains using FIFO
            for buy in buys:
                for sell in sells:
                    quantity = min(sell[0], buy[0])
                    gains += quantity*(sell[1] - buy[1])
                    sell[0] -= quantity
                    if sell[0] != 0:
                        break
        return gains
    else:
        raise ValueError("Incorrect type")




class DistributionForm(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.db = db

        self._data = []
        self._data.append(self.load_type(ttypes[0]))
        self._data.append(self.load_type(ttypes[1]))
        self._data.append(self.load_type(ttypes[2]))
        self._data.append(self.load_type(ttypes[3]))

        calculate_gains(self.db, "Stock")
        #print(self._data)

    def load_type(self, stype):
        sql_msg = self.db.transactions.select_by_type(stype)
        entries = self.db.query(sql_msg)
        entries = self.parse_data(entries)
        total_invested = self.get_total_invested(entries)
        #current_value = self.get_current_value(entries)
        return entries

    def parse_data(self, data):
        data_parsed = []
        for i in range(0, len(data)):
            entry = list(data[i])
            data_parsed.append(entry)
        return data_parsed

    # Interesting colums are 
    # 3: Buy/Sell
    # 5: Quantity
    # 6: Unit price
    # 8: Exchange rate
    # 9: Fee
    # 11: Exchange rate
    def get_total_invested(self, data):
        total = 0
        for entry in data:
            amount_core = entry[5]*entry[6]*entry[8]
            amount_fee = entry[9]*entry[11] 
            amount_total = amount_core + amount_fee
            if entry[3] == 'Buy':
                total += amount_total
            elif entry[3] == "Sell":
                pass
            else:
                raise ValueError("Type was not either Buy or Sell!")
        return total
        
    # Interesting columns are
    # 3: Buy/Sell
    # 5: Quantity
    # 6: Currency
    # 14&15&16: name, ticker, and country
    # 17: type
    # 18: method
    def get_current_value(self, data):
        total = 0
        for entry in data:
            pass

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

