

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.4
import QtQuick3D 6.4
import QtQuick.Window 6.4
//import QtQuick.Controls.Material
import QtQuick.Controls 6.4
import "../imports/UntitledProject"
import Qt.SafeRenderer 2.0

Pane {

    property double sc_joint1: 400
    property double sc_joint2: 90
    property double sc_joint3: 90
    property color view3d_color: "#ffffff"
    id: root
    width: 1530
    height: 780

    Item {
        id: __materialLibrary__
    }
    Rectangle {
        color: view3d_color
        x: 1045
        y: 2
        width: 460
        height: 402
        View3D {
            id: view3D
            anchors.fill: parent
            anchors.leftMargin: -88
            anchors.topMargin: -84
            scale: 1
            anchors.rightMargin: -23
            anchors.bottomMargin: -103

            environment: sceneEnvironment

            SceneEnvironment {
                id: sceneEnvironment
                antialiasingMode: SceneEnvironment.MSAA
                antialiasingQuality: SceneEnvironment.High
            }
            Robot {
                scale_x: 1
                scale_y: 1
                scale_z: 1
                robot_joint1: sc_joint1
                robot_joint2: sc_joint2
                robot_joint3: sc_joint3
            }
        }
    }
}
