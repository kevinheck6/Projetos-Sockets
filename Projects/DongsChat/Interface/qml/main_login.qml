import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material


// Main window
ApplicationWindow {
    id: window
    width: 500
    height: 580
    visible: true
    title: qsTr("Login")

    //Flags

    // Material styles
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    QtObject {
        id: internal
        property string user: "teste@hotmail.com"
        property string pass: "123"

        function checkLogin(username, password) {
            if (username == user && password == pass) {
                var components = Qt.createComponent("dashboard.qml")
                var wind = components.createObject()
                wind.show()
                visible = false
            } else {
                // Change USER Color
                if(username != user) {
                    username_field.Material.foreground = Material.Red
                    username_field.Material.accent = Material.Red
                } else {
                    username_field.Material.foreground = Material.LightBlue
                    username_field.Material.accent = Material.LightBlue
                }

                // Change PASSWORD Color
                if(password != pass) {
                    password_field.Material.foreground = Material.Red
                    password_field.Material.accent = Material.Red
                } else {
                    password_field.Material.foreground = Material.LightBlue
                    password_field.Material.accent = Material.LightBlue
                }

            }
        }
    }

    Rectangle {
        id: topBar
        height: 50
        color: "#202024"
        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
            margins: 10
        }
        radius: 3

        Text {
            id: text
            text: qsTr("Login")
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignmentCenter
            verticalAlignment: Text.AlignmentCenter
            color: "#FFFFFF"
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 20
        }
    }

    Image {
        id: image
        width: 150
        height: 150
        source: "../images/logo.png"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: topBar.bottom
        anchors.margins: 60
    }

    TextField {
        id:username_field
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("Seu nome de usuario")
        verticalAlignment: text.AlignVCenter

        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: image.bottom
        anchors.margins: 60
    }

    
    TextField {
        id: password_field
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("Sua senha")
        verticalAlignment: text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: username_field.bottom
        anchors.topMargin: 10 
        echoMode: TextInput.Password
    }

    CheckBox {
        id: check_box
        text: qsTr("Salvar sua senha")
        anchors.top: password_field.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Button {
        id: button_login
        width: 300
        text: qsTr("Logar")
        anchors.top: check_box.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: internal.checkLogin(username_field.text, password_field.text)
    }
}