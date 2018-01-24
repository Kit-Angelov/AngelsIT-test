from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from messages import *


def main():
    import sys

    sys_argv = sys.argv
    sys_argv += ['--style', 'material']

    app = QGuiApplication(sys_argv)

    listMessages = ListMessages()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('listMessages', listMessages)
    engine.load('main.qml')

    exit(app.exec_())


if __name__ == '__main__':
    main()
