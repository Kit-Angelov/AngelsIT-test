
from dbutils import SqliteDB
from datetime import date
from config import *


class DataGetterSetter:
    """
    Обработчики запросов, умеют обращаться к бд
    """

    def __init__(self):
        self.db = SqliteDB(db_name)

    def getShops(self):
        list_shops = self.db.get_shops()
        return list_shops

    def getProducts(self, shop_id):
        list_products = self.db.get_products(shop_id)
        return list_products

    def getBasket(self):
        basket_id = self.db.add_basket(date.today())
        return basket_id

    # обработка данных со списком товаров для добавления в элементы корзины
    def handleData(self, data):
        basket_id = ''
        print('Список продуктов: ')
        for item in data:
            self.db.add_basket_elem(item['count'], item['product_id'], item['basket_id'])
            basket_id = item['basket_id']
            print(item)
        # print('Продукты к покупке: ')
        # for item in self.sqliteDB.get_basket_elems(basket_id):
        #     print(item)
