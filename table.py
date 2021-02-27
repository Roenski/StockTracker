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

    def select_all(self, num, offset=0):
        sql_msg = "SELECT * FROM transactions " \
        + "ORDER BY tid ASC LIMIT {} OFFSET {}".format(num, offset)
        return sql_msg

    def delete_entry(self, tid):
        sql_msg = "DELETE FROM WHERE tid={}".format(tid)
        return sql_msg
        
class StockTable:

    def __init__(self):
        pass 

    def select_all(self, num, offset=0):
        sql_msg = "SELECT * FROM stocks" \
        + "ORDER BY sid ASC LIMIT {} OFFSET {}".format(num, offset)
        return sql_msg

    def delete_entry(self, sid):
        sql_msg = "DELETE FROM stocks WHERE sid={}".format(sid)
        return sql_msg
