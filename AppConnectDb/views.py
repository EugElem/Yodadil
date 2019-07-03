from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from .models import Position
from .models import Search
from .connector import con_db
from .putSearch import fSearch
import sqlite3
import re


#счетчик поисковых запросов сеанса
counter =[]
saver=[]


# получение данных из бд
def index(request):

    return render(request, "index.html")



# получение ответа на поисковый запрос
def create(request):

    put = fSearch()
    search_drug = put

    if request.method == "POST":
        counter.append(1) # итерация счетчика поисковых запросов
        counterLen = counter.__len__()

        # Отправка в БД введеного поискового запроса
        ser = Search()
        ser.name = request.POST.get("search")
        ser.requestNumber =  counterLen # передача счетчика в бд

        ser.save()
        print("счетчик = ", counterLen)

        # подключение к базе
        connect = sqlite3.connect('db.sqlite3')
        cursor = connect.cursor()



        cursor.execute("SELECT name FROM AppConnectDb_search")
        nameSearch = cursor.fetchall()
        nSearch = str(nameSearch[-1])  # получение последнего элемента из базы пользовательского ввода
        nSearch = re.sub(u'[(\',)]', "", nSearch)  # удаление лишних символов ('  и ',)
        nSearch = nSearch.lower()   # перевод вех символов в нижний регистр
        nSearch = nSearch.title()  # первый символ - в заглавный
        #print(nSearch)

        print('saver: ' + str(saver)+'  '+ str(saver.__len__))
        print("counter: ",str(counterLen - 1))
        if ((saver ==[])&(counterLen>0)):
            req ="DELETE FROM AppConnectDb_position WHERE counter = "+ str(counterLen-1)
            print("req: ", req)
            cursor.execute(req)
            connect.commit()
        else:
            # отключение сейвера на следующий цикл (если сейвер пустой - сохранения не будет)
            saver.clear()


        # вызов функции соединения с БД
        con_db(nSearch, counterLen)

        print('поиск препарата (данные из БД): ', nSearch)

        # Аналогично SELECT * FROM Position ORDER BY price WHERE price >0 (WHERE price >0 реализован в filter)
        preparat = Position.objects.filter(price__gt=0, counter__in=str(counterLen)).order_by('price')
        if re.search('Position object',str(preparat)):
           print("препарат: preparat",preparat)
        else:
            print("препарат не найден ")
        connect.close()
    return render(request, "index.html", {"preparat": preparat})


# Очистка списка
def back (request):
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute("DELETE  FROM AppConnectDb_position")
    connect.commit()
    connect.close()

    Position.objects.all().delete()
    return HttpResponsePermanentRedirect("/")


# Перход на страницу заказа
def buy (request):
    buyRequest = request.POST.get("link")
    print('будет заказан ', buyRequest)
    import webbrowser
    webbrowser.open_new_tab(buyRequest)

    return HttpResponsePermanentRedirect("/")


# Добавить в список поиска
def save (request):
    saver.append(1)
    return HttpResponsePermanentRedirect("/")



"""
# вывод всего списка
def getlist(request):

    put = fSearch()

    if request.method == "POST":


        ser = Search()
        ser.name = request.POST.get("search")
        ser.requestNumber =  counterLen # передача счетчика в бд

        ser.save()
        print("счетчик = ", counterLen)
        # здесь типа ковычки
        
        
        # здесь пользовательский ввод из сохоаненного в базе
        ##connect = sqlite3.connect('db.sqlite3')
        ##cursor = connect.cursor()

        
        # здесь типа ковычки
        cursor.execute("SELECT name FROM AppConnectDb_search")
        nameSearch = cursor.fetchall()
        nSearch = str(nameSearch[-1])  # получение последнего элемента из базы пользовательского ввода
        nSearch = re.sub(u'[(\',)]', "", nSearch)  # удаление лишних символов ('  и ',)
        nSearch = nSearch.lower()   # перевод вех символов в нижний регистр
        nSearch = nSearch.title()  # первый символ - в заглавный
        #print(nSearch)

        print('saver: ' + str(saver)+'  '+ str(saver.__len__))
        if ((saver ==[])&(counterLen>0)):
            req ="DELETE FROM AppConnectDb_position WHERE counter = "+ str(counterLen-1)
            print(req)
            cursor.execute(req)
            connect.commit()
        else:
            saver.clear()
        # здесь типа ковычки

        # вызов функции соединения с БД
        ##con_db(nSearch, counterLen)

        ##print('поиск препарата (данные из БД): ', nSearch)

        # Аналогично SELECT * FROM Position ORDER BY price WHERE price >0 (WHERE price >0 реализован в filter)
        preparat = Position.objects.filter(price__gt=0).order_by('price')
        if re.search('Position object',str(preparat)):
           print("препарат: preparat",preparat)
        else:
            print("препарат не найден ")
        ##connect.close()

    return render(request, "index.html", {"preparat": preparat})
    """