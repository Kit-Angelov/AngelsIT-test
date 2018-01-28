import sys
from socket import *
import json
from config import *
from models import *


"""
    Класс с методами общения с сервером
"""


class ClientSender:

    def __init__(self):
        self.host = host
        self.port = port
        self.addr = addr
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)

    def sendToServer(self, data):
        self.tcp_socket.connect(self.addr)

        if not data:
            self.tcp_socket.close()
            sys.exit(1)

        data = str.encode(data)
        self.tcp_socket.send(data)
        self.tcp_socket.close()

    def requestShops(self):
        self.tcp_socket.connect(self.addr)
        data = 'get_shops'
        data = str.encode(data)
        self.tcp_socket.send(data)
        data = self.tcp_socket.recv(1024)
        if not data:
            self.tcp_socket.close()
        else:
            self.tcp_socket.close()
            data = bytes.decode(data)
            data = json.loads(data)
            return data

    def requestProducts(self, shop_id):
        self.tcp_socket.connect(self.addr)
        data = 'get_products ' + str(shop_id)
        data = str.encode(data)
        self.tcp_socket.send(data)
        data = self.tcp_socket.recv(1024)
        if not data:
            self.tcp_socket.close()
        else:
            self.tcp_socket.close()
            data = bytes.decode(data)
            data = json.loads(data)
            return data

    def requestBasket(self):
        self.tcp_socket.connect(self.addr)
        data = 'get_basket'
        data = str.encode(data)
        self.tcp_socket.send(data)
        data = self.tcp_socket.recv(1024)
        if not data:
            self.tcp_socket.close()
        else:
            self.tcp_socket.close()
            data = bytes.decode(data)
            return data



