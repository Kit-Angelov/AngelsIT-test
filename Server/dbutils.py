import sqlite3


class SqliteDB:

    def __init__(self, db_name):
        print(db_name)
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    # создание таблицы с магазинами
    def create_table_shops(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS shops
                                                                  (id INTEGER PRIMARY KEY, 
                                                                  name_shop TEXT NOT NULL,
                                                                  img_path VARCHAR(34))
                                                                  """)

    #  создание таблицы продуктов
    def create_table_products(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY,
                                                                    name_product TEXT NOT NULL,
                                                                    price REAL,
                                                                    shop_id INTEGER NOT NULL,
                                                                    FOREIGN KEY (shop_id) REFERENCES shops(id)
                                                                    )
                                                                    """)

    # создание таблицы корзин
    def create_table_baskets(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS baskets(
                                                                        id INTEGER PRIMARY KEY,
                                                                        create_date DATE NOT NULL
                                                                        )""")

    # создание таблицы элементов корзины
    def create_table_basket_elems(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS basket_elems(
                                                                        id INTEGER PRIMARY KEY,
                                                                        count_product INTEGER NOT NULL,
                                                                        product_id INTEGER NOT NULL,
                                                                        basket_id INTEGER NOT NULL,
                                                                        FOREIGN KEY (product_id) REFERENCES products(id),
                                                                        FOREIGN KEY (basket_id) REFERENCES baskets(id)
                                                                        )""")

    # добавление магазина
    def add_shop(self, id, name_shop, img_path):
        with self.connection:
            self.cursor.execute("""INSERT INTO shops (id, name_shop, img_path) 
                                                                        VALUES(%s, '%s', '%s')""" % (id, name_shop, img_path))

    # получение данных о магазине
    def get_shops(self):
        with self.connection:
            self.cursor.execute("""SELECT * FROM shops""")
        return self.cursor.fetchall()

    # добавление продуктов
    def add_product(self, name_product, price, shop_id):
        with self.connection:
            self.cursor.execute("""INSERT INTO products (name_product, price, shop_id) 
                                                            VALUES('%s', %s, %s)""" % (name_product, price, shop_id))

    # получение продуктов
    def get_products(self, shop_id):
        with self.connection:
            self.cursor.execute("""SELECT * FROM products WHERE shop_id = %s""" % shop_id)
        return self.cursor.fetchall()

    # добавление корзины
    def add_basket(self, create_date):
        with self.connection:
            self.cursor.execute("""INSERT INTO baskets (create_date) VALUES('%s')""" % create_date)
        return self.cursor.lastrowid

    # получение корзины
    def get_basket(self, id):
        with self.connection:
            self.cursor.execute("""SELECT * FROM baskets WHERE id = %s""" % id)
        return self.cursor.fetchall()[0]

    # добавление элементов корзины
    def add_basket_elem(self, count_product, product_id, basket_id):
        with self.connection:
            self.cursor.execute("""INSERT INTO basket_elems (count_product, product_id, basket_id) 
                                                        VALUES(%s, %s, %s)""" % (count_product, product_id, basket_id))

    # получение элементов корзины
    def get_basket_elems(self, basket_id):
        with self.connection:
            self.cursor.execute("""SELECT * FROM basket_elems WHERE basket_id = %s""" % basket_id)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()