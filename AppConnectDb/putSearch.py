import sqlite3
import  re

def fSearch():
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    #cursor.execute("DELETE FROM AppConnectDb_search")  # исполняем SQL-запрос
    #cursor.execute("""INSERT INTO AppConnectDb_search(name, requestNumber)VALUES('%(name)s', '%(requestNumber)s')
    #""" % {"name":"drug","requestNumber":0}
    #               )
    #connect.commit()  # применяем изменения к базе данных

    cursor.execute("SELECT name FROM AppConnectDb_search")
    nameSearch = cursor.fetchall()
    nSearch = str(nameSearch[-1]) # получение последнего элемента
    nSearch = re.sub(u'[(\']|[\',)]', "", nSearch)  # удаление лишних символов ('  и ',)

    print('поиск препарата данные из БД: ', nSearch)


    connect.close()
    return nSearch


