from clientSender import ClientSender
from models import *

"""
    Обработчики запросов, вынесенные в отдельную библиотеку, для разделения логики работы с представлениями и 
    логики работы общения с сервером
"""


def getShops():
    clientSender = ClientSender()
    list_shops = clientSender.requestShops()
    list_shops_obj = list()
    for item in list_shops:
        list_shops_obj.append(Shop(id=item[0], name_shop=item[1], img_path=item[2]))
    return list_shops_obj


def getProducts(shop_id):
    clientSender = ClientSender()
    list_products = clientSender.requestProducts(shop_id)
    list_products_obj = list()
    for item in list_products:
        list_products_obj.append(Product(id=item[0], name_product=item[1], price=item[2], shop_id=item[3]))
    return list_products_obj


def createBasket():
    clientSender = ClientSender()
    basket_id = clientSender.requestBasket()
    return basket_id


def postBasket(data):
    clientSender = ClientSender()
    clientSender.sendToServer(data)