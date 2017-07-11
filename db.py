import MySQLdb
class DB:
    @staticmethod
    def connect():
        connection = MySQLdb.connect(host='localhost', user='slivinskiy', passwd='', db='c9', charset='utf8')
        return connection
