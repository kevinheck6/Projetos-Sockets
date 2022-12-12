import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow {
    visible: true
    width: 500
    height: 400
    font.pixelSize: 24
    Material.theme: "Dark"


    Row {
        id: row
        spacing: 20
        anchors {
            horizontalCenter: parent.horizontalCenter
            topMargin: 20
        }
    }

    TextField {
        placeholderText: "Insira seu Login"
        width: 200
    }

    Text {
        text: "Arquivo"
    }

    Button {
    text: "Name"
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    width: 200
    height: 100
    }
}