import QtQuick 2.9
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.1
import QtQuick.Controls.Material 2.3
import QtQuick.Window 2.0


ApplicationWindow {
    id: window
    visible: true
    width: 800
    height: 600
    Component.onCompleted: {
        setX(Screen.width / 2 - width / 2);
        setY(Screen.height / 2 - height / 2);
    }
    Material.theme: Material.Light
    Material.accent: Material.blue
    Material.primary: Material.Indigo

    header: ToolBar{
        RowLayout{
            anchors.fill: parent
            Label {
                text: "Test"
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignLeft
                leftPadding: 10
                font.pointSize: 14
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
            ToolButton {
                text: qsTr("\u22EE")
                onClicked: popup.open()
           }
        }
    }

    Popup {
        id: popup
        x: window.width / 2 - width / 2
        y: window.height / 2 - height
        width: 300
        height: 200
        modal: true
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent | Popup.CloseOnReleaseOutside

        Text {
            anchors.centerIn: parent
            verticalAlignment: Qt.AlignCenter
            horizontalAlignment: Qt.AlignCenter
            text: "version: 1.0\nTest for AngelsIt"
        }
    }

    ColumnLayout {
        anchors.fill: parent

        Pane {
            anchors.fill: parent
            Layout.fillWidth: true
            Layout.fillHeight: true
            Component {
                id: contentDelegate
                Pane {
                    width: parent.width
                    Material.background: "transparent"
                    Pane {
                        Material.background: "white"
                        Material.elevation: 4
                        width: parent.width - 10
                        height: parent.height + 10
                        topPadding: 8
                        bottomPadding: 0
                        Text {
                            width: parent.width
                            text: content
                            font.pointSize: 12
                            verticalAlignment: Qt.AlignVCenter
                            wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                        }
                    }
                }
            }
            }
            ListView {
                clip: true
                flickableDirection: Flickable.VerticalFlick
                Layout.fillHeight: true
                Layout.fillWidth: true
                anchors.fill: parent
                model: listMessages.messages
                delegate: contentDelegate
                ScrollBar.vertical: ScrollBar {}
            }

        Pane {
            id: pane
            Layout.fillWidth: true
            RowLayout {
                width: parent.width
                TextArea {
                    id: messageField
                    Layout.fillWidth: true
                    placeholderText: qsTr("Введите текст")
                    Material.accent: Material.Blue
                    wrapMode: TextArea.Wrap
                }
                Button {
                    id: addButton
                    text: qsTr("Добавить")
                    enabled: messageField.length > 0
                    onClicked: {
                        listMessages.addMessage(messageField.text)
                        messageField.text = ""
                    }
                }
                Button {
                    id: sendButton
                    text: qsTr("Отправить")
                    highlighted: true
                    enabled: listMessages.messages.length > 0
                    onClicked: {
                        listMessages.sendMessage()
                    }
                }
            }
        }
    }
}
