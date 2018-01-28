import QtQuick 2.9
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.1
import QtQuick.Controls.Material 2.3
import QtQuick.Window 2.0

Page {
    id: shops
    property  string nameShop
    header: ToolBar{
        RowLayout{
            anchors.fill: parent
            ToolButton {
                text: "\u25C0"
                onClicked: stack.pop()
            }
            Label {
                text: nameShop
                elide: Label.ElideRight
                leftPadding: 10
                font.pointSize: 14
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
            ToolButton {
                text: qsTr("Корзина")
                rightPadding: 10
                onClicked: {
                    stack.push('basket.qml')
                }
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
                        RowLayout {
                            width: parent.width
                            Text{
                                font.pointSize: 14
                                text: "<b>" + name_product + "</b>" + " ("+ price + " руб.)"
                                Layout.fillWidth: true
                            }
                            SpinBox{
                               id: countBox
                               value: 1
                               from: 1
                               to: 10
                            }
                            Button {
                                id: sendButton
                                text: qsTr("В корзину")
                                highlighted: true
                                onClicked: {
                                    listBasketElems.addProduct(countBox.value, id, name_product, price)
                                }
                            }
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
            model: listProducts.products
            delegate: contentDelegate
            ScrollBar.vertical: ScrollBar {}
        }
    }
}
