from PyQt5.QtQml import QQmlListProperty
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
import json
from clientSender import ClientSender
from clientGetter import ClientGetter


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


class ListShops(QObject):
    listShops = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._shops = []
        self.setShops()

    def setShops(self):
        clientGetter = ClientGetter()
        shops = clientGetter.getShops()
        for item in shops:
            self._shops.append(Shop(item))

    @pyqtProperty(QQmlListProperty,notify=listShops)
    def shops(self):
        return QQmlListProperty(Shop, self, self._shops)

    chooseShopSignal = pyqtSignal(int, arguments=['chooseShop'])

    @pyqtSlot(int)
    def chooseShop(self, arg):
        print('arg', arg)
        listProducts.setProducts(arg)


class Product(QObject):
    contentNameProduct = pyqtSignal()
    contentPrice = pyqtSignal()

    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name_product = product.name_product
        self._price = product.price
        self._shop_id = product.shop_id

    @pyqtProperty('QString', notify=contentNameProduct)
    def name_product(self):
        return self._name_product

    @pyqtProperty('QString', notify=contentPrice)
    def price(self):
        return self._price


class ListProducts(QObject):

    listProducts = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._products = []

    def setProducts(self, shop_id):
        clientGetter = ClientGetter()
        products = clientGetter.getProducts(shop_id)
        self._products = []
        for item in products:
            self._products.append(Product(item))
        self.listProducts.emit()

    @pyqtProperty(QQmlListProperty, notify=listProducts)
    def products(self):
        return QQmlListProperty(Product, self, self._products)


class Message(QObject):

    contentMessage = pyqtSignal()

    def __init__(self, content='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._content = content

    @pyqtProperty('QString', notify=contentMessage)
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if content != self._content:
            self._content = content
            self.contentMessage.emit()


class ListMessages(QObject):

    listMessages = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._messages = []

    @pyqtProperty(QQmlListProperty, notify=listMessages)
    def messages(self):
        return QQmlListProperty(Message, self, self._messages)

    @messages.setter
    def messages(self, messages):
        if messages != self._messages:
            self._messages = messages
            self.listMessages.emit()

    def appendMessage(self, message):
        self._messages.append(message)
        self.listMessages.emit()

    addMessageSignal = pyqtSignal(str, arguments=['addMessage'])

    @pyqtSlot(str)
    def addMessage(self, arg):
        self.appendMessage(Message(arg))

    sendMessageSignal = pyqtSignal(arguments=['sendMessage'])

    @pyqtSlot()
    def sendMessage(self):
        data = json.dumps([item.content for item in self._messages])
        sender = ClientSender()
        sender.sendToServer(data)
        self._messages = []
        self.listMessages.emit()


class Init:
    listShops = ListShops()
    listProducts = ListProducts()
