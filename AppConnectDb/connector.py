# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3
import AppConnectDb.parser
import re

p = AppConnectDb.parser

# переменные для получения к ним доступа в view.py
arr = p.arr
arr1 =p.arr1
arr2 =p.arr2
requ =[]
cookieList = []
idNet_1 = []
url = []



def con_db(search_drug, counter):

    # Создаем соединение с нашей базой данных
    conn = sqlite3.connect('db.sqlite3')

    """ id аптечной сети (удаление лишнего)"""
    def fNet (idNet):
        for i in range (0, len(idNet)):
            temp = str(idNet[i])
            temp = re.sub(u'[(]|[,)]', "", temp)
            idNet_1.append(temp)
            #print('idNet_1[',i,']= ', idNet_1[i])
        return idNet_1


    """ куки из БД (удаление лишнего)"""
    def fCookie (result):
        cookieList.clear()
        i = 0
        # цикл обработки ответа базы данных
        # получение из списка отдельных, готовых к отправке cookies
        for result_single in result:
            result_temp = str(result_single)  # преобразование кортежа в строку
            result_temp = re.sub(u'[(\']|[\')]', "", result_temp) # удаление лишних символов ('  и ',)
            cookieList.append(result_temp) #запись в список куки
            i = i + 1
        return cookieList

    """ url для соединения с искомым сайтом (удаление лишнего) """
    def fUrls (urls):
        for i in range (0, len(urls)):
            temp = str(urls[i])
            temp = re.sub(u'[(\']|[\')]', "", str(temp))
            url.append(temp)
            #print('url[',i,']= ', url[i])
        return url


    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()

    # получение id сети из БД
    cursor.execute("SELECT id FROM AppConnectDb_drugshopnet")
    idNet = cursor.fetchall()
    fNet(idNet)

    # получение url из БД
    cursor.execute("SELECT urlNet, pathNet , nameNet, id FROM AppConnectDb_drugshopnet")
    urls = cursor.fetchall()
    #print("url & path: ", urls)
    fUrls(urls)

    # получение значения счетчика из бд
    cursor.execute("SELECT requestNumber FROM AppConnectDb_search ")
    coun = cursor.fetchall()
    requ = str(coun[-1])
    requ = re.sub(u'[(]|[,)]', "",requ)

    for i in range (0,len(idNet)):
        # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
        mySelect = "SELECT cookie FROM AppConnectDb_mycookie WHERE idNet ="+ idNet_1[i]
        cursor.execute(mySelect)
        results = cursor.fetchall()     # Получаем результат сделанного запроса
        #print('results = ',type(results),' ',results)

        fCookie(results)

        # теперь cookies могут быть отправлены на сайт
        p.pars(url[i], cookieList, search_drug, counter)

    print('+++++++++++++++++++++++++++++вызов парсера из коннектора+++++++++++++++++++++++++++++++++')
    # создание sql  запроса
    print('length: ',len(p.arr))
    for i in range(0, len(p.arr)-1):
        print('Препарат:', p.arr[i], '  Цена:',p.arr1[i],'  ссылка:', p.arr2[i])
        insert ="""INSERT INTO AppConnectDb_position
        (id, product, price, link, requ) VALUES ('%(id)s','%(prod)s','%(pri)s','%(lin)s','%(requ)s')""" \
                % {"id":(i+1),"prod":p.arr[i],"pri":p.arr1[i],"lin":p.arr2[i],"requ":requ}

        cursor.execute(insert) # исполняем SQL-запрос
        conn.commit() # применяем изменения к базе данных

    # закрыть соединение с базой данных
    conn.close()
    return arr, arr1, arr2


def con_buy(buyRequest):
    # получение id сети из БД
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM AppConnectDb_drugshopnet")
    idNet = cursor.fetchall()

    for i in range (0,len(idNet)):
        # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
        mySelect = "SELECT cookie FROM AppConnectDb_mycookie WHERE idNet ="+ idNet_1[i]
        cursor.execute(mySelect)
        results = cursor.fetchall()     # Получаем результат сделанного запроса
        #print('results = ',type(results),' ',results)