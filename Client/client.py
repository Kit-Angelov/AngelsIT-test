from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from QtModels import *


def main():
    import sys

    sys_argv = sys.argv
    sys_argv += ['--style', 'material']

    app = QGuiApplication(sys_argv)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('listShops', listShops)
    engine.rootContext().setContextProperty('listProducts', listProducts)
    engine.rootContext().setContextProperty('listBasketElems', listBasketElems)
    engine.load('Client/views/shops.qml')

    exit(app.exec_())


if __name__ == '__main__':
    main()
