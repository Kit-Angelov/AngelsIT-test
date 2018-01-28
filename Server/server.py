import json
from socket import *

from Client.config import *
from dbutils import SqliteDB


class DataHandler:

    def __init__(self):
        self.sqliteDB = SqliteDB()
        self.sqliteDB.create_table_messages()

    def handleData(self, data):
        print('Новые сообщения: ')
        for item in data:
            print(item)
            self.sqliteDB.add_message(item)
        print('Сообщения в базе: ')
        for item in self.sqliteDB.get_messages():
            print(item[0])


class SocketListener:

    def __init__(self):
        self.host = host
        self.port = port
        self.addr = addr
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.bind(self.addr)
        self.tcp_socket.listen()

    def run(self, dataHandler):
        while True:
            print('\nв ожидании...\n')

            conn, addr = self.tcp_socket.accept()
            print('клиент: ', addr)

            data = conn.recv(1024)
            if not data:
                conn.close()
                break
            else:
                conn.close()
                data = bytes.decode(data)
                data = json.loads(data)
                dataHandler.handleData(data)
        self.stop()

    def stop(self):
        self.tcp_socket.close()


def main():
    dataHandler = DataHandler()
    listener = SocketListener()
    listener.run(dataHandler)


if __name__ == '__main__':
    main()