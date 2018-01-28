import json
from socket import *
from config import *
from dataGetter import DataGetterSetter


class SocketListener:

    def __init__(self):
        self.host = host
        self.port = port
        self.addr = addr
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.bind(self.addr)
        self.tcp_socket.listen()
        self.dataGetterSetter = DataGetterSetter()

    def run(self):
        while True:
            print('\nв ожидании...\n')
            conn, addr = self.tcp_socket.accept()
            print('клиент: ', addr)

            data = conn.recv(1024)
            if not data:
                conn.close()
                break
            else:
                data = bytes.decode(data)
                """
                    Получение сообщения от клиента и его обработка
                """
                if data == 'get_shops':
                    new_data = self.dataGetterSetter.getShops()
                    new_data = json.dumps(new_data)
                    new_data = str.encode(new_data)
                    conn.send(new_data)
                    conn.close()
                    continue
                if data.startswith('get_products'):
                    shop_id = data.split(' ')[1]
                    new_data = self.dataGetterSetter.getProducts(int(shop_id))
                    new_data = json.dumps(new_data)
                    new_data = str.encode(new_data)
                    conn.send(new_data)
                    conn.close()
                    continue
                if data == 'get_basket':
                    new_data = self.dataGetterSetter.getBasket()
                    new_data = str.encode(str(new_data))
                    conn.send(new_data)
                    conn.close()
                    continue
                else:
                    conn.close()
                    data = json.loads(data)
                    self.dataGetterSetter.handleData(data)
                    continue
        self.stop()

    def stop(self):
        self.tcp_socket.close()


def main():
    listener = SocketListener()
    listener.run()


if __name__ == '__main__':
    main()