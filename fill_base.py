from Server.dbutils import SqliteDB

db = SqliteDB()

shops = [
    {'id': 1, 'name_shop': 'Пятерочка', 'img_path': 'media/5chka.png'},
    {'id': 2, 'name_shop': 'Пятью Пять', 'img_path': 'media/55.jpg'},
    {'id': 3, 'name_shop': 'Billa', 'img_path': 'media/billa.jpg'},
    {'id': 4, 'name_shop': 'Магнит', 'img_path': 'media/magnit.jpg'},
]

products = [
    {'shop_id': 1, 'name_product': 'Батон', 'price': 32},
    {'shop_id': 1, 'name_product': 'Яйца', 'price': 68},
    {'shop_id': 1, 'name_product': 'Квас', 'price': 89},
    {'shop_id': 1, 'name_product': 'Сыр', 'price': 349},
    {'shop_id': 2, 'name_product': 'Хлеб', 'price': 25},
    {'shop_id': 2, 'name_product': 'Рыба', 'price': 215},
    {'shop_id': 3, 'name_product': 'Сметана', 'price': 64},
    {'shop_id': 3, 'name_product': 'Пельмени', 'price': 228},
    {'shop_id': 3, 'name_product': 'Сыр', 'price': 287},
    {'shop_id': 4, 'name_product': 'Батон', 'price': 22},
    {'shop_id': 4, 'name_product': 'Майонез', 'price': 56},
    {'shop_id': 4, 'name_product': 'Колбаса', 'price': 184},
]


def createdb():
    db.create_table_shops()
    db.create_table_products()
    db.create_table_baskets()
    db.create_table_basket_elems()


def fill_shops(attrs):
    for item_dict in attrs:
        db.add_shop(id=item_dict['id'], name_shop=item_dict['name_shop'], img_path=item_dict['img_path'])


def fill_products(attrs):
    for item_dict in attrs:
        db.add_product(name_product=item_dict['name_product'], price=item_dict['price'], shop_id=item_dict['shop_id'])

createdb()
fill_shops(shops)
fill_products(products)