from django.db import models

# модель хранения пользовательского ввода
class Search(models.Model):
    name = models.CharField(max_length=100)             # имя искомого препарата
    requestNumber =models.IntegerField(max_length=10)  # номер запроса

# модель для хранения информации о позициях
class Position(models.Model):
    # id позиции
    id = models.IntegerField
    # инф. по позиции (название, дозировка, количество)
    product = models.CharField(max_length=50)
    # цена
    price = models.IntegerField(max_length=20)
    # аптечная сеть
    net = models.CharField(max_length=127)
    # ссылка на страницу заказа
    link = models.CharField(max_length=127)
    # счетчик заказов
    counter = models.IntegerField(max_length=10)




# модель для хранения куки id (города)
class MyCookie(models.Model):
    # id cookie
    id = models.IntegerField
    # название АС
    idNet = models.IntegerField(max_length=10)
    # куки
    cookie = models.CharField(max_length=127)

# модель для хранения url аптечных сетей
class DrugShopNet(models.Model):
    # id сети
    idNet = models.IntegerField
    # название Аптечной сети
    nameNet = models.CharField(max_length=20)
    # город парсинга
    town = models.CharField(max_length=10)
    # url для соединения с сетью
    urlNet = models.CharField(max_length=127)
    # дополнение к url
    pathNet = models.CharField(max_length=127)



# модель для хранения url аптечных сетей
class Pattern(models.Model):
    # создание связи 1 к 1
    drugShopNet = models.OneToOneField(DrugShopNet, on_delete=models.CASCADE)

    # тег ссылки
    link_tag = models.CharField(max_length=50)
    # класс ссылки
    class_link = models.CharField(max_length=127)
    # регулярка ссылки
    link_re = models.CharField(max_length=50)

# тег цены
    class_price = models.CharField(max_length=127)
    # класс цены
    price_tag = models.CharField(max_length=50)
    # регулярка цены
    price_re = models.CharField(max_length=127)
    # регулярка цены (окончание)
    price_re_end = models.CharField(max_length=127)

    # тег позиции
    product_tag = models.CharField(max_length=50)
    # сласс позиции
    class_name = models.CharField(max_length=127)
    # регулярка позиции
    product_re = models.CharField(max_length=127)
    # регулярка позиции (окончание)
    product_re_end = models.CharField(max_length=127)