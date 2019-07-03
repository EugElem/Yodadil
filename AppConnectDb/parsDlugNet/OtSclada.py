#import AppConnectDb.parser
import re


#class OtSclada(AppConnectDb.parser):
#print("Годовалов")

#arr = []
#arr1 = []
#arr2 = []

#  функция парсить ссылки
def parse_link(soup):
    arr2 = []
    class_link = "product-main"
    links = soup.find_all('div', class_=class_link)

    for link in links:
        link = link.find('a').get('href')
        link = "https://apteka-ot-sklada.ru" + link
        print('link: ', link)

        arr2.append(link)
    # print('arr2: ', arr2)
    return arr2

def parse_product(soup):
    arr = []
    class_product1 = "product-name"  # Годовалов

    product = soup.find_all('a', class_=class_product1)
    #print('Год продЖ ', product)
    # заполнение массива правильно, исключая "Поиск", а также у Годовалова присваивание правельных индексов
    i = 0
    l = len(product)

    #print('l (Годовалов) = ', l)
    for product_single in product:
        product_single = product_single.text.strip()  # strip - для удаления тегов. остается только  значение между тегами
        #print('product_single: ', product_single)

        arr.append(product_single)
        # print('arr:   ',arr)
        print('arr[', i, ']', arr[i])
        i += 1
    return arr

def parse_price(soup):
    arr1 = []
    priceIf = soup.div(class_="product-info")

    for l in priceIf:
        l_print=l
        #print('l_print=l.contents: ', l_print)
        if re.search( '"product-price"', str(l_print)):

            price_single = l_print.find_next('span', class_="product-price")
            #print('price_single: ', price_single)
            price_single1 = price_single.text.strip()  # strip - для удаления тегов. остается только  значение между тегами
            price_single1 = int(re.sub('\D\d*', "", price_single1))
            print('ЦЕНА ', price_single1)

        else:
            print("нет в наличии ")
            price_single1 = 0


        arr1.append(int(price_single1))

    return arr1

