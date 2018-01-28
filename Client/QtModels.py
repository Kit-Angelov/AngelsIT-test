import json
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtQml import QQmlListProperty
from clientSender import ClientSender
from dataGetter import *
from models import *


# Обьект магазина
class Shop(QObject):
    contentNameShop = pyqtSignal()
    contentImgPath = pyqtSignal()
    contentId = pyqtSignal()

    def __init__(self, shop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name_shop = shop.name_shop
        self._img_path = shop.img_path
        self._id = str(shop.id)

    @pyqtProperty('QString', notify=contentNameShop)
    def name_shop(self):
        return self._name_shop

    @pyqtProperty('QString', notify=contentImgPath)
    def img_path(self):
        return self._img_path

    @pyqtProperty('QString', notify=contentId)
    def id(self):
        return self._id


# обьект списка магазинов
class ListShops(QObject):
    listShops = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._shops = []
        self.setShops()

    def setShops(self):
        shops = getShops()
        for item in shops:
            self._shops.append(Shop(item))

    @pyqtProperty(QQmlListProperty,notify=listShops)
    def shops(self):
        return QQmlListProperty(Shop, self, self._shops)

    chooseShopSignal = pyqtSignal(int, arguments=['chooseShop'])

    @pyqtSlot(int)
    def chooseShop(self, arg):
        listProducts.setProducts(arg)


# обьект продукта
class Product(QObject):
    contentNameProduct = pyqtSignal()
    contentPrice = pyqtSignal()
    contentId = pyqtSignal()

    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = str(product.id)
        self._name_product = product.name_product
        self._price = str(product.price)
        self._shop_id = str(product.shop_id)

    @pyqtProperty('QString', notify=contentNameProduct)
    def name_product(self):
        return self._name_product

    @pyqtProperty('QString', notify=contentPrice)
    def price(self):
        return self._price

    @pyqtProperty('QString', notify=contentId)
    def id(self):
        return self._id


# обьект списка продуктов
class ListProducts(QObject):

    listProducts = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._products = []

    def setProducts(self, shop_id):
        products = getProducts(shop_id)
        self._products = []
        for item in products:
            self._products.append(Product(item))
        self.listProducts.emit()

    @pyqtProperty(QQmlListProperty, notify=listProducts)
    def products(self):
        return QQmlListProperty(Product, self, self._products)


# обьект элемента корзины
class BasketElem(QObject):
    contentCount = pyqtSignal()
    contentBasketId = pyqtSignal()
    contentProductId = pyqtSignal()
    contentProductName = pyqtSignal()
    contentProductPrice = pyqtSignal()
    contentCost = pyqtSignal()

    def __init__(self, basket_elem, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._count = str(basket_elem.count_product)
        self._basket_id = str(basket_id)
        self._product_id = str(basket_elem.product_id)
        self._product_name = str(basket_elem.product_name)
        self._product_price = str(basket_elem.product_price)
        self._cost = str(basket_elem.cost)

    @pyqtProperty('QString', notify=contentCount)
    def count(self):
        return self._count

    @pyqtProperty('QString', notify=contentBasketId)
    def basket_id(self):
        return self._basket_id

    @pyqtProperty('QString', notify=contentProductId)
    def product_id(self):
        return self._product_id

    @pyqtProperty('QString', notify=contentProductName)
    def product_name(self):
        return self._product_name

    @pyqtProperty('QString', notify=contentProductPrice)
    def product_price(self):
        return self._product_price

    @pyqtProperty('QString', notify=contentCost)
    def cost(self):
        return self._cost


# обьект списка элементов корзины
class ListBasketElems(QObject):

    listBasketElems = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._basket_elems = []

    @pyqtProperty(QQmlListProperty, notify=listBasketElems)
    def basket_elems(self):
        return QQmlListProperty(BasketElem, self, self._basket_elems)

    def appendProduct(self, basket_elem):
        self._basket_elems.append(basket_elem)
        self.listBasketElems.emit()

    addProductSignal = pyqtSignal(int, int, str, str, arguments=['addProduct'])

    @pyqtSlot(int, int, str, str)
    def addProduct(self, arg1, arg2, arg3, arg4):
        basket = Basket_elem(arg1, arg2, basket_id, arg3, arg4)
        self._basket_elems.append(BasketElem(basket))
        self.listBasketElems.emit()

    sendBaketSignal = pyqtSignal(arguments=['sendBasket'])

    @pyqtSlot()
    def sendBasket(self):
        data = json.dumps([{"product_id": item.product_id,
                            "basket_id": basket_id,
                            "count": item.count} for item in self._basket_elems])
        postBasket(data)
        self._basket_elems = []
        self.listBasketElems.emit()

    deleteBasketElemSignal = pyqtSignal(int, arguments=['deleteBasketElem'])

    @pyqtSlot(int)
    def deleteBasketElem(self, arg):
        x = self._basket_elems.pop(arg)
        self.listBasketElems.emit()


# ничего лучше не придумал как проинициализировать обьекты тут, т.к. была необходимость обращаться к обьектам Qt
# из других обьектов в ходе выполнения программы
basket_id = createBasket()
listShops = ListShops()
listProducts = ListProducts()
listBasketElems = ListBasketElems()
