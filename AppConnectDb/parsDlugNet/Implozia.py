import re

#  функция парсить ссылки
def parse_link(soup, class_link, url, link_tag, link_re):

    link_tag = re.sub('\s','',link_tag)

    print("link_tag: ", link_tag)

    arr2 = []
    # поиски нужного <dev> в супе
    links = soup.find_all(link_tag, class_=class_link)
    #print("class_link: ", class_link)
    #print("link_soup: ", links)



     # tag & atribute нужно поместить в БД.
    print("link_re: ", link_re )

    tag_L = 'a'
    atribute_L = 'href'


    for link in links:
        if (re.search("(href=\"http)|(href=\"/)", str(link))):
            link = link.find(tag_L).get(atribute_L)
            if (re.search("^/", link)):
                link = url+link
            print('Ссылка: ', str(link))

        else:
            print('Ссылка не найдена ',str(link))

        arr2.append(link)
        #print('arr2: ', arr2)

    return arr2




#################################################################
def parse_product(soup, class_name, search1, product_tag, product_re, product_re_end):


    search = re.sub(u'[(\',)]', "", search1)  # удаление лишних символов ( ',) "
    search = search.lower()  # перевод вех символов в нижний регистр
    search = search.title()  # первый символ - в заглавный
    #print("search: "+search)

    class_product = re.sub("^ ", "", class_name)
    #print("class_product: ", class_product)
    arr = []

    # удаление лишних пробелов
    product_tag1 = re.sub('^\s','',product_tag)
    product_re1 = re.sub('^\s','',product_re)
    product_re_end1 = re.sub('^\s','',product_re_end)
    product_re2 = product_re1+'[\s\d\D]*'+product_re_end1


    print("product_tag1: ", product_tag1)
    products = soup.find_all(product_tag1, class_=class_product)
    #print("products: ", products)



    # разбор содержимого <div></div> на входящие в него теги и поиск в них искомой строки

    i=0
    for product in products:

        product_single = re.search(product_re2,str(product))
        #print("product_single", product_single)
        product_single = str(product.text.strip())
        ##product_re1 = "^\d\D\s"+product_re1
        product_re_end1 = product_re_end1+"[\d\D\s]*"
        ##product_single = re.search(product_re1, str(product_single))
        ##print("product_single", str(product_single))
        product_single = re.sub(product_re_end1,"", str(product_single))
        ##print("product_single", product_single)

        arr.append(product_single)
        print('arr[', i, ']', arr[i])
        print("----------------")
        i += 1

    return arr




############################################################
def parse_price(soup,class_price, price_tag, price_re, price_re_end):

    class_price1 = re.sub('^\s', "", class_price)   # удаление лишних пробелов
    price_tag1 = re.sub('^\s','',price_tag)         # удаление лишних пробелов
    price_re1 = re.sub('^\s','',price_re)           # удаление лишних пробелов
    price_re_end1 = re.sub('^\s','',price_re_end)           # удаление лишних пробелов


    arr1 = []

    # Поиск в супе  по тегу price_tag из БД с классом class_price1 тоже из БД
    priceIf = soup.find_all(price_tag1, class_=class_price1)

    #print("priceIf: ", priceIf)


    print("price_re1: ", price_re1)
    print("price_re_end1: ", price_re_end1)


    # добавдение к переменнной регулярке постоянной части
    pr_re = price_re1+'[\s\d\D]*'+ price_re_end1
    print("pr_re: ", pr_re)

    # Поиск в <div> цены и удаление лишнего
    for price1 in priceIf:

        if(re.search(pr_re, str(price1))):
            pars = re.search(pr_re, str(price1))
            print("pars: ", pars)
            #print("\n strPrice: ", price1)
            # удаление копеек
            pars =re.sub("\.\d{2}","",pars.group())
            print("pars: ", pars)

            if (re.search("\d", str(price1))):
                pars1 = re.sub("\D+" , "" , pars)
            elif (re.search("[^\d]", str(price1))):
                pars1 = 0
                #pars1 = int(pars1)
            else:
                print("непонятная ошибка")


        else:
            print("Не найден")
            pars1 = 0

        """
        if (re.search("[^\d+]",pars1)):
            print("Нет в наличии")
            p=0
            pars1=p
            <div class="catalog-item__price">
            <div class="price-list-item__price"><div class="price-list-item__buy-btn js-add-to-cart">
        """
        print("ЦЕНА ", pars1)

        arr1.append(int(pars1))
        print('arr1: ', arr1)
    return arr1

