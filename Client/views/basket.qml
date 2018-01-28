import QtQuick 2.9
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.1
import QtQuick.Controls.Material 2.3
import QtQuick.Window 2.0

Page {
    id: basket
    property  string nameShop
    header: ToolBar{
        RowLayout{
            anchors.fill: parent
            ToolButton {
                text: "\u25C0"
                onClicked: stack.pop()
            }
            Label {
                text: "Корзина"
                elide: Label.ElideRight
                leftPadding: 10
                font.pointSize: 14
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
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
            id: mainContent
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
                        RowLayout {
                            width: parent.width
                            Text {
                                width: parent.width
                                text: "<b>" + product_name + "</b>" + " (" + product_price + " руб.) Кол-во: " + count + " шт. стоимость: <b>" + cost + "руб.</b>"
                                font.pointSize: 12
                                Layout.fillWidth: true
                                verticalAlignment: Qt.AlignVCenter
                                wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                            }
                            RoundButton {
                                id: sendButton
                                text: qsTr("x")
                                highlighted: false
                                onClicked: listBasketElems.deleteBasketElem(index)
                            }
                        }
                    }
                }
            }
            }
        ListView {
            id: listViewBasketElems
            clip: true
            flickableDirection: Flickable.VerticalFlick
            Layout.fillHeight: true
            Layout.fillWidth: true
            anchors.fill: parent
            model: listBasketElems.basket_elems
            delegate: contentDelegate
            ScrollBar.vertical: ScrollBar {}
        }
        Pane {
            id: panePay
            Layout.fillWidth: true
            Layout.fillHeight: true
            RowLayout {
                width: parent.width
//                TextArea {
//                    id: messageField
//                    Layout.fillWidth: true
//                    placeholderText: qsTr("Введите номер телефона")
//                    Material.accent: Material.Blue
//                    wrapMode: TextArea.Wrap
//                }
                Rectangle {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    color: "transparent"
                }

                Button {
                    id: sendButton
                    text: qsTr("Оформить покупку")
                    highlighted: true
                    enabled: listViewBasketElems.model.length > 0
                    onClicked: {
                        listBasketElems.sendBasket()
                    }
                }
            }
        }
    }
}
