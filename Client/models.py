"""
    Представление обьектов системы в виде питоновских классов
    Для удобства работы с сущностями в представлениях QT обьектов
"""


class Shop:

    def __init__(self, id, name_shop, img_path):
        self.name_shop = name_shop
        self.img_path = img_path
        self.id = id

    def __repr__(self):
        return '{} {}'.format(str(self.id), self.name_shop, self.img_path)


class Product:

    def __init__(self, id, name_product, price, shop_id):
        self.id = id
        self.name_product = name_product
        self.price = price
        self.shop_id = shop_id

    def __repr__(self):
        return '{} {} {}'.format(self.name_product, str(self.price), str(self.shop_id))


class Basket:

    def __init__(self, id, create_date):
        self.create_date = create_date
        self.id = id

    def __repr__(self):
        return '{} {}'.format(str(self.id), str(self.create_date))


class Basket_elem:

    def __init__(self, count_product, product_id, basket_id, product_name, product_price):
        self.count_product = count_product
        self.product_id = product_id
        self.basket_id = basket_id
        self.product_name = product_name
        self.product_price = product_price
        self.cost = float(self.product_price) * int(self.count_product)

    def __repr__(self):
        return '{} {} {}'.format(str(self.count_product), str(self.product_id), str(self.basket_id))
