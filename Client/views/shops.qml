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
    StackView {
        id: stack
        initialItem: shops
        anchors.fill: parent
    }
    Page {
        id: shops
        header: ToolBar{
            RowLayout{
                anchors.fill: parent
                Label {
                    text: "Магазины"
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
                padding: 0
                Component {
                    id: contentDelegate
                    Pane {
                        width: grid.cellWidth
                        height: grid.cellHeight
                        Material.background: "transparent"
                        Pane {
                            Material.background: "white"
                            width: parent.width - 10
                            height: parent.height + 10
                            Material.elevation: mouseArea.containsMouse ? 7 : 2
                            padding: 0
                            Image{
                                width: parent.width
                                height: parent.height
                                source: img_path
                                fillMode: Image.PreserveAspectCrop
                            }
                            MouseArea {
                                id: mouseArea
                                anchors.fill: parent
                                hoverEnabled: true
                                onClicked: {
                                    stack.push('products.qml', {'nameShop': name_shop})
                                    listShops.chooseShop(id)
                                }
                            }
                        }
                    }
                }
            }
            GridView {
                id: grid
                clip: true
                flickableDirection: Flickable.VerticalFlick
                Layout.fillHeight: true
                Layout.fillWidth: true
                cellWidth: 400; cellHeight: 250
                model: listShops.shops
                delegate: contentDelegate
                ScrollBar.vertical: ScrollBar {}
            }
        }
    }
}
