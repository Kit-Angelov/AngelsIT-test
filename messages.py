from PyQt5.QtQml import QQmlListProperty
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
import json
from clientSender import ClientSender


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