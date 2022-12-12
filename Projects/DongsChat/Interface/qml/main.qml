import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material


// Main window
Window {
    id: main
    width: 800
    height: 580
    visible: true
    title: qsTr("DongsChat: " + username)
    color: "#151515"
}