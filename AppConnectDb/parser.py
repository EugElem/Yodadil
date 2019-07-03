from bs4 import BeautifulSoup
import requests
import re
import json
import sqlite3
import AppConnectDb.parsDlugNet.Planet
import AppConnectDb.parsDlugNet.OtSclada
import AppConnectDb.parsDlugNet.Implozia


arr = []
arr1 = []
arr2 = []

arr02 = []
arr12 = []
arr22 = []

Pl = AppConnectDb.parsDlugNet.Planet
Ot = AppConnectDb.parsDlugNet.OtSclada
Im = AppConnectDb.parsDlugNet.Implozia

def pars(url_path, cookieList, search_drug, counter):


    path =[]
    # заголовок - информация о браузере
    headers = {'user-agent': 'your-own-user-agent/0.0.1'}
    i=0
    url_1 = re.split(r',', url_path)
    url = url_1[0]
    print('url: ', url)
    path = re.sub('"',"",url_1[1])
    path = re.sub(" ","",path)
    print('path: ', path)
    net = re.sub('"',"",url_1[2])
    net = re.sub(" ","",net)
    print('net: ', net)
    idDrNet = re.sub('"|\s', "", url_1[3])
    print('netId: ', idDrNet)

    # соединение с БД
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # получение паттернов для парсинга из БД

    patt = "SELECT class_link, class_price, class_name, " \
           "product_tag, price_tag, price_re, " \
           "link_tag, link_re, product_re, " \
           "price_re_end, product_re_end FROM AppConnectDb_pattern WHERE id =" +"\"" +idDrNet+"\""

    #print("patt: ", patt)
    cursor.execute(patt)
    patterns = cursor.fetchall()
    #print("patterns: ", patterns)
    patterns=str(patterns)
    patterns_1 = re.sub(u'[\(\'\)]', "", patterns)  # удаление лишних  ( ',)]["
    patterns_1 = re.sub('^(\[)|(\]$)', '', patterns_1)
    patterns_1=re.split(",",patterns_1)

    print("class_link: ",  patterns_1 [0]) # class_link
    print("link_tag: ",    patterns_1 [6]) # link_tag
    print("link_re: ",     patterns_1 [7]) # link_re

    print("class_price: ", patterns_1 [1]) # class_price
    print("price_tag: ",   patterns_1 [4]) # price_tag
    print("price_re: ",    patterns_1 [5]) # price_re
    print("price_re_end:", patterns_1 [9]) # price_re_end

    print("class_name: ",  patterns_1 [2]) # class_name
    print("product_tag: ", patterns_1 [3]) # product_tag
    print("product_re: ",  patterns_1 [8]) # product_re
    print("product_re_end:",patterns_1 [10]) # product_re_end







    """
    первый запрос куков !!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    # создание сессии подключения
    s = requests.Session()
    s.get(url)


    # новые значения куков
    for cookie_single1 in cookieList:
        cookie_single1 = re.sub(',$', "", cookie_single1)
        cookie_single = json.loads(cookie_single1)

        # устанавливаю новые куки
        s.cookies.set(**cookie_single)

    s.post(url=url, headers=headers, cookies=s.cookies)
    #s.get(url=url, headers=headers, cookies=s.cookies)


    """
    запрос после установки куков !!!!!!!!!!!!!!!!!!!!!!!!!!   
    """
    cookies = 0 # на всякий случай обнуляю cookies

    n1 = search_drug # поисковый запрос
    url_single = url + path+ n1 # получение строки для поиска
    #print('url_single: ', url_single)
    w =0
    w = s.get(url=url_single, headers=headers, cookies=cookies) # получение куков


    """
    Отлов цены
    """
    # Парсим страницу с помощью BeautifulSoup
    soup = BeautifulSoup(w.text, features="html.parser")


    # вызов функции получения ссылок
    """
    if url == "https://apteka.planetazdorovo.ru":
        arr2 = Pl.parse_link(soup)
        arr  = Pl.parse_product(soup)
        arr1 = Pl.parse_price(soup)
    """

        #elif url =="https://apteka-ot-sklada.ru":
        #arr2 = Ot.parse_link(soup)
        #arr  = Ot.parse_product(soup)
        #arr1 = Ot.parse_price(soup)

    #else:
    arr2 = Im.parse_link(soup, patterns_1[0], url, patterns_1[6], patterns_1[7])
    arr  = Im.parse_product(soup, patterns_1[2], search_drug, patterns_1[3], patterns_1[8], patterns_1[10])
    arr1 = Im.parse_price(soup, patterns_1[1], patterns_1[4], patterns_1[5], patterns_1[9])



    print('+++++++++++++++++++++++++++++Внесение в базу+++++++++++++++++++++++++++++++++')
    # создание sql  запроса
    print('length: ', len(arr))
    for i in range(0, len(arr)):
        print('Препарат:', arr[i], '  Цена:', arr1[i], '  ссылка:', arr2[i])
        insert = """INSERT INTO AppConnectDb_position
           (product, price, link, net, counter) VALUES ('%(prod)s','%(pri)s','%(lin)s','%(net)s','%(cou)s')""" \
                 % {"prod": arr[i], "pri": arr1[i], "lin": arr2[i],"net": net,"cou": counter}
        print('Запись № ',i,' внесена в базу')
        print("---------------Работа с сетью ", net, " выполнена-----------------")

        cursor.execute(insert)  # исполняем SQL-запрос
        conn.commit()  # применяем изменения к базе данных
    conn.close()


def pars_link(search_drug):
    pars(search_drug)
    return arr2

def pars_product(search_drug):
    pars(search_drug)
    return arr

def pars_price(search_drug):
    pars(search_drug)
    return arr1
