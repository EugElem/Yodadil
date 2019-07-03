#import AppConnectDb .parser
import re

#class Planet(AppConnectDb .parser):
#print("Опека")


#arr =[]
#arr1=[]
#arr2=[]

 #  функция поиска ссылки
def parse_link(soup):
    arr2 = []
    class_link = "product-card__title"
    links = soup.find_all('div', class_=class_link)

    for link in links:
        link = link.find('a').get('href')
        print('link: ', link)

        arr2.append(link)
        #print('arr2: ', arr2)
    return arr2



    # функция получения названия препаратов и занесения в список arr

def parse_product(soup):
    arr = []
    class_product = "name"  # Опека
    product = soup.find_all('span', itemprop=class_product)

    # заполнение массива правильно, исключая "Поиск", а также у Годовалова присваивание правельных индексов
    i = 0
    l = len(product)-1

    #print('l (Опека) = ',l)
    for product_single in product:
        product_single = product_single.text.strip()  # strip - для удаления тегов. остается только  значение между тегами
        #print('product_single: ', product_single)

        if product_single != 'Поиск': # возможно это только для Опеки
            arr.append(product_single)
            #print('arr:   ',arr)
            print('arr[',i,']', arr[i])
            i+=1
    return arr





    # функция получения цен и занесения в список arr1

def parse_price(soup):
    arr1 = []
    class_price = "product-card__price"

    price = soup.find_all('div', class_=class_price)
    #print('price: ', price)

    for price_single in price:
        price_single = price_single.text.strip()  # strip - для удаления тегов. остается только  значение между тегами
        price_single1 = re.sub('\D', "", price_single)
        print('ЦЕНА ', price_single1)
        arr1.append(int(price_single1))
    return arr1

