import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material


// Main window
ApplicationWindow {
    id: window
    width: 700
    height: 600
    visible: true
    title: qsTr("DashBoard")

    //Flags

    // Material styles
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue
}