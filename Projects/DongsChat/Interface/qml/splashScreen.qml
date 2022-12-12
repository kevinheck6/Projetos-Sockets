import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material
import Qt5Compat.GraphicalEffects

import "components"

// Main window
Window {
    id: splashScreen
    width: 380
    height: 580
    visible: true
    title: qsTr("DongsChat:" )
    
    // Remove tittle bar
    flags: Qt.Window | Qt.FramelessWindowHint

    // Internal functions

    // timers

    // Objects
    Rectangle {
        id: bg
        x: 78
        y: 131
        width: 360
        height: 560
        color: "#151515"
        radius: 3
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        z: 1

        CircularProgressBar {
            id: circularProgressBar
            x: 55
            y: 198
            opacity: 0

            anchor.verticalCenter: parent.verticalCenter
            value: 100
            progressWidth: 8
            strokeBgWidth: 4
            progressColor: "#67AA25"

            anchors.horizontalCenter: parent.horizontalCenter
        }
    }


}