from dbutils import SqliteDB
from models import *


class DataGetter:

    def __init__(self):
        self.db = SqliteDB()

    def getShops(self):
        list_shop_db = self.db.get_shops()
        list_shop_obj = list()
        for item in list_shop_db:
            shop = Shop(id=item[0], name_shop=item[1], img_path=item[2])
            list_shop_obj.append(shop)
        return list_shop_obj

    def getProducts(self, shop_id):
        list_product_db = self.db.get_products(shop_id)
        list_product_obj = list()
        for item in list_product_db:
            product = Product(name_product=item[1], price=str(item[2]), shop_id=shop_id)
            list_product_obj.append(product)
        return list_product_obj
