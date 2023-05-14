import QtQuick 6.4
import QtQuick.Controls.Material
import QtQuick.Controls 6.4
Rectangle{
    width: 1530
    height: 780
    property color color_text: "#000000"
    property color textinput_color: "#ffff66"
    property int text_size: 15

    property bool status_m1
    property bool status_plc
    property bool status_camera

//    color: "red"
//    border.color: "black";
    color: "transparent"
    border.color: "#000000"

    Rectangle{
        id:m1
        Rectangle {
            id: rectangle
            x: 35
            y: 22
            width: 121
            height: 24
            color: textinput_color
            TextInput {
                id: ip_m1
                enabled: !status_m1
                x: 0
                y: 0
                width: 120
                height: 22
                text: qsTr("192.168.31.171")
//                text: qsTr(status_m1)
                color: color_text
                font.pixelSize: text_size
            }
        }
        Rectangle {
            id: rectangle1
            x: 201
            y: 23
            width: 50
            height: 24
            color: textinput_color
            TextInput {
                id: port_m1
                enabled: !status_m1
                x: 3
                y: 0
                width: 45
                height: 24
                color: color_text
                text: qsTr("8080")
                font.pixelSize: text_size
            }
        }
        Button {
            id: con_m1
            x: 261
            y: 15
            width: 150
            height: 40
            text: status_m1 ? "DisConnect M1":"Connect M1"
            font.pixelSize: text_size
            background: Rectangle {
                radius: 70
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
            }
            onClicked: {
                python.send("m1 "+ip_m1.text+" "+port_m1.text)
            }
        }



        Text {
            id: text1
            x: 20
            y: 21
            width: 19
            height: 23
            text: qsTr("IP")
            font.pixelSize: text_size
            color: color_text
        }

        Text {
            id: text2
            x: 162
            y: 24
            width: 44
            height: 20
            text: qsTr("PORT")
            font.pixelSize: text_size
            color: color_text
        }
    }
    Rectangle{
        id:plc
        x:0
        y:-25
        Button {
            id: con_plc
            x: 262
            y: 78
            width: 150
            height: 40


            text: status_plc ? "DisConnect PLC":"Connect PLC"
            font.pixelSize: text_size
            background: Rectangle {
                radius: 70
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
            }
            onClicked: {
                python.send("plc "+ip_plc.text+" "+port_plc.text)
            }
        }
        Rectangle {
            id: rectangle2
            x: 36
            y: 89
            width: 121
            height: 24
            color: textinput_color
            TextInput {
                id: ip_plc
                enabled: !status_plc
                x: 0
                y: 0
                width: 128
                height: 24
                text: qsTr("192.168.31.171")
                //        color:color_text
                color: color_text
                font.pixelSize: text_size
            }
        }
        Rectangle {
            id: rectangle3
            x: 202
            y: 90

            width: 50
            height: 24
            color: textinput_color
        TextInput {
            id: port_plc
            enabled: !status_plc
            x: 2
            y: 1
            width: 45
            height: 25
            color: color_text
            text: qsTr("502")
            font.pixelSize: text_size
        }
        }

        Text {
            id: text1_plc
            x: 20
            y: 88
            width: 20
            height: 25
            text: qsTr("IP")
            font.pixelSize: text_size
            color: color_text
        }

        Text {
            id: text2_plc
            x: 161
            y: 89
            width: 40
            height: 28
            text: qsTr("PORT")
            font.pixelSize: text_size
            color: color_text
        }
    }

    Rectangle{
        id:camera
        x:0
        y:12

        Button {
            id: con_camera
            x: 262
            y: 78
            width: 150
            height: 40


            text: status_camera ? "Disconnect Cam":"Connect Cam"
            font.pixelSize: text_size
            background: Rectangle {
                radius: 70
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
            }
            onClicked: {

//             myImageProvider.select_cam(ip_camera.text)

//                console.log(ip_camera.text)

                python.send("camera "+ip_camera.text)
                status_camera ? myImageProvider.killThread():myImageProvider.start(ip_camera.text)
                if(myImageProvider.get_camera_accept() === 1){
                python.send("camera_set "+"1")
                }else if (myImageProvider.get_camera_accept() === 0){
                   python.send("camera_set "+"0")
                }


            }
        }

        Rectangle {
            id: rectangle4
            x: 73
            y: 89
            width: 183
            height: 24
            color: textinput_color
            TextInput {
                id: ip_camera
                enabled: !status_camera
                x: 4
                y: 0
                width: 179
                height: 24
                text: qsTr("2")
                //        color:color_text
                color: color_text
                font.pixelSize: text_size
            }
        }

        Text {
            id: text1_camera
            x: 20
            y: 88
            width: 20
            height: 25
            text: qsTr("Camera")
            font.pixelSize: text_size
            color: color_text
        }

    }
    Timer {
        interval: 25; running: true; repeat: true
        onTriggered: {
            status_m1 = python.return_m1()
            status_plc = python.return_plc()
            status_camera =python.return_camera()
            myImageProvider.get_cam(status_camera)


//            console.log((status_camera))
        }
    }

}
