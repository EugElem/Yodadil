import re
import sqlite3

#class NaKrups(AppConnectDb.parser):
#print("На Крупской")

idDrNet = "3"  # передать сюда при вызове функции нопер АС


#  функция парсить ссылки
def parse_link(soup):

    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute("SELECT class_link FROM AppConnectDb_drugshopnet WHERE id ="+"\"" +idDrNet+"\"")
    class_link = cursor.fetchall()
    cursor.execute("SELECT urlNet FROM AppConnectDb_drugshopnet WHERE id ="+"\"" +idDrNet+"\"")
    urlNet = cursor.fetchall()
    connect.close()

    arr2 = []
    links = soup.find_all('div', class_=class_link)

    for link in links:
        link = link.find('a').get('href')
        print('link: ', link)
        arr2.append(link)

    # print('arr2: ', arr2)
    return arr2




def parse_product(soup):
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()

    cursor.execute("SELECT class_name FROM AppConnectDb_drugshopnet WHERE id =" + "\"" + idDrNet + "\"")
    class_product1 = str(cursor.fetchall())
    class_product = str(re.sub(u'[(\'",[\])]', "", class_product1))  # удаление лишних  ( ',)]["
    #print("class_product: "+class_product)

    cursor.execute("SELECT name FROM AppConnectDb_search WHERE id = (SELECT MAX(id) FROM main.AppConnectDb_search)")
    search1 = str(cursor.fetchall())
    search = re.sub(u'[(\',)]', "", search1)  # удаление лишних символов ( ',) "
    search = search.lower()  # перевод вех символов в нижний регистр
    search = search.title()  # первый символ - в заглавный
    #print("search: "+search)

    arr = []
    products = soup.find_all('div', class_=class_product)
    #print("products: " + str(products))

    # разбор содержимого <div></div> на входящие в него теги и поиск в них искомой строки
    i=0
    for product in products:
        product_single = str(product.text.strip())
        if (re.search(search,product_single)):
            arr.append(product_single)
            print('arr[', i, ']', arr[i])
            i += 1
    return arr





def parse_price(soup):

    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute("SELECT class_price FROM AppConnectDb_drugshopnet WHERE id = "+"\"" +idDrNet+"\"")
    class_price1 = str(cursor.fetchall())
    class_price = str(re.sub(u'[(\'",[\])]', "", class_price1))  # удаление лишних  ( ',)]["
    print("class_price1: "+ class_price)

    arr1 = []
    priceIf = soup.find_all('div',class_=class_price)
    #print("priceIf: "+str(priceIf))
    connect.close()

    class_price_1 = "\"" + class_price + "\""
    print("class_price_1: " + class_price_1)

    # Поиск в <div> цены и удаление лишнего
    i=0
    for price1 in priceIf:

        if(re.search("<div class=\"product-card__price\">\s+\d+",str(price1))):
            pars = re.search("<div class=\"product-card__price\">\s+\d+", str(price1))
            pars1 = re.sub("\D+","",pars.group())

            print("price1 !!!!: "+ pars1)
            print()
        else:
            print("Не найден")
            pars1 = 0


        arr1.append(int(pars1))

    return arr1

