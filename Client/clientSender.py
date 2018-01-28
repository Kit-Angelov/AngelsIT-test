from socket import *
import sys
from config import *


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
