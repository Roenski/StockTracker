class Table:
    def __init__(self):
        pass

    def select_all(self):
        raise NotImplementedError

    def delete_entry(self):
        raise NotImplementedError


class TransactionTable:

    def __init__(self):
        pass

    def get_count_of_bs(self, tbs, ttype, sticker):
        sql_msg = "SELECT SUM(squantity) FROM transactions "\
        + "WHERE (tbs='{}' AND ttype='{}' AND sname='{}')".format(
            tbs, ttype, sticker
        )
        return sql_msg

    def select_all(self, num, offset=0):
        sql_msg = "SELECT * FROM transactions " \
        + "ORDER BY tdate ASC LIMIT {} OFFSET {}".format(num, offset)
        return sql_msg

    # Buy/Sell
    def select_by_bs(self, tbs):
        sql_msg = "SELECT * FROM transactions " \
            + "INNER JOIN stocks ON transactions.sname = stocks.sticker " \
            + "WHERE transactions.tbs = '{}'".format(tbs)
        return sql_msg

    def select_by_bs_type_name(self, tbs, ttype, sticker):
        sql_msg = "SELECT * FROM transactions " \
            + "INNER JOIN stocks ON transactions.sname = stocks.sticker " \
            + "WHERE (transactions.tbs = '{}' ".format(tbs) \
            + "AND transactions.ttype = '{}'".format(ttype) \
            + "AND stocks.sticker = '{}') ".format(sticker) \
            + "ORDER BY transactions.tdate"
        return sql_msg

    def select_by_bs_and_type(self, tbs, ttype):
        sql_msg = "SELECT * FROM transactions " \
            + "INNER JOIN stocks ON transactions.sname = stocks.sticker " \
            + "WHERE (transactions.tbs = '{}' ".format(tbs) \
            + "AND transactions.ttype = '{}')".format(ttype)
        return sql_msg

    # type = ETF, Stock, Fund, Crypto etc..
    def select_by_type(self, ttype):
        sql_msg = "SELECT * FROM transactions " \
        + "INNER JOIN stocks ON transactions.sname = stocks.sticker " \
        + "WHERE transactions.ttype = '{}' ".format(ttype) 
        return sql_msg

    def select_names_by_type(self, ttype):
        sql_msg = "SELECT DISTINCT sname FROM transactions " \
        + "WHERE ttype = '{}'".format(ttype) 
        return sql_msg

    def delete_entry(self, tid):
        sql_msg = "DELETE FROM transactions WHERE tid={}".format(tid)
        return sql_msg
        
class StockTable:

    def __init__(self):
        pass 

    def select_all(self, num, offset=0):
        sql_msg = "SELECT * FROM stocks " \
        + "ORDER BY stype, sname ASC LIMIT {} OFFSET {}".format(num, offset)
        return sql_msg

    def select_tickers(self, stype=""):
        sql_msg = "SELECT sticker FROM stocks" 
        if stype:
            sql_msg += " WHERE stype = '{}'".format(stype)
        return sql_msg

    def get_type(self, ticker):
        sql_msg = "SELECT stype FROM stocks WHERE sticker = '{}'".format(ticker)
        return sql_msg

    def get_method(self, ticker):
        sql_msg = "SELECT smethod FROM stocks WHERE sticker = '{}'".format(ticker)
        return sql_msg

    def get_full_name(self, ticker):
        sql_msg = "SELECT sname FROM stocks WHERE sticker = '{}'".format(ticker)
        return sql_msg

    def get_country(self, ticker):
        sql_msg = "SELECT scountry FROM stocks WHERE sticker = '{}'".format(ticker)
        return sql_msg

    def delete_entry(self, sid):
        sql_msg = "DELETE FROM stocks WHERE sid={}".format(sid)
        return sql_msg
