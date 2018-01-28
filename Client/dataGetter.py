from Server.dbutils import SqliteDB


class DataGetter:

    def __init__(self):
        self.db = SqliteDB()

    def getShops(self):
        list_shops = self.db.get_shops()
        return list_shops

    def getProducts(self, shop_id):
        list_products = self.db.get_products(shop_id)
        return list_products
