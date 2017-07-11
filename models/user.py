from db import DB
class User:
    @staticmethod
    def check(login):
        connection = DB.connect()
        cursor = connection.cursor()
        sql = """SELECT login FROM users WHERE login = %s"""
        cursor.execute(sql, login)
        data =  cursor.fetchall()
        connection.commit()
        connection.close()
        return data

    @staticmethod
    def add(login, password):
        connection = DB.connect()
        cursor = connection.cursor()
        args = login, password
        sql = """INSERT INTO users VALUES (%s, %s)"""
        execute = cursor.execute(sql, args)
        connection.commit()
        connection.close()
        return True

    @staticmethod
    def getUsers():
        connection = DB.connect()
        cursor = connection.cursor()
        sql = 'SELECT * FROM users'
        cursor.execute(sql)
        data =  cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def delete(login):
        connection = DB.connect()
        cursor = connection.cursor()
        sql = 'DELETE FROM users WHERE login = %s'
        cursor.execute(sql, login)
        data =  cursor.fetchall()
        connection.commit()
        connection.close()
        return data

    @staticmethod
    def checkPassword(login, password):
        connection = DB.connect()
        cursor = connection.cursor()
        args = login, password
        sql = 'SELECT * FROM users WHERE login = %s AND password = %s'
        cursor.execute(sql, args)
        data =  cursor.fetchall()
        connection.commit()
        connection.close()
        return data
