import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle{
    width: 1530
    height: 780
    property int size_conveyor: 25
    property color text_color: "#000000"
    property string f_s_r: "0 0"
    color: "transparent"

    Rectangle{
        x: 0
        y: 159
        width: 413
        height: 282
        color: "transparent"
        Rectangle{
            x: 203
            y: 52
            width: 4
            height: 223
            color: text_color
        }
//        border.color: "black"
//        border.width: 4
        Button {
            id: text_title
            x: 0
            y: 7
            width: 413
            height: 55
            text: "PLC control"
            font.pixelSize: 40
            background: Rectangle {
                color: "#7DCF73"
                radius: 0
            }
            onClicked: {

            }
        }

        Rectangle{
            x: 203
            y: 93
            width: 210
            height: 189
            border.color: text_color
            border.width: 4
             color: "transparent"

            Button {
                id: plc1_forward
                x: 41
                y: 8
                width: 133
                height: 54
                text: "Forward"//forward
                font.pixelSize: text_size
                background: Rectangle {
                    radius: 15
                    color: f_s_r[2] === "1" ? "#0038c7":"#1aa7ff"
                }
                onClicked: {
                    python.write_plc("11")

                }
            }
            Button {
                id: plc1_stop
                x: 41
                y: 68
                width: 133
                height: 54
                text: "Stop"
                font.pixelSize: text_size
                background: Rectangle {
                   radius: 15
                  color: f_s_r[2] === "0" ? "#0038c7":"#1aa7ff"
                }
                onClicked: {
                    python.write_plc("10")

                }
            }
            Button {
                id: plc1_reverse
                x: 41
                y: 128
                width: 133
                height: 54
                text: "Reverse"
                font.pixelSize: text_size
                background: Rectangle {
                    radius: 15
                    color: f_s_r[2] === "2" ? "#0038c7":"#1aa7ff"
                }
                onClicked: {
                    python.write_plc("12")
                }
            }
        }

        Rectangle {
            x: 0
            y: 93
            width: 207
            height: 189
            border.color: text_color
            border.width: 4
            color: "transparent"

            Button {
                id: plc2_forward
                x: 33
                y: 8
                width: 133
                height: 54
                text: "Forward"
                font.pixelSize: text_size
                background: Rectangle {
                    color: f_s_r[0] === "1" ? "#0038c7":"#1aa7ff"

                    radius: 15
                }
                onClicked: {
                    python.write_plc("01")


                }
            }

            Button {
                id: plc2_stop
                x: 33
                y: 68
                width: 133
                height: 54
                text: "Stop"
                font.pixelSize: text_size
                background: Rectangle {
                   color: f_s_r[0] === "0" ? "#0038c7":"#1aa7ff"
                   radius: 15
                }
                onClicked: {
                    python.write_plc("00")
                }
            }

            Button {
                id: plc2_reverse
                x: 33
                y: 128
                width: 133
                height: 54
                text: "Reverse"
                font.pixelSize: text_size
                background: Rectangle {
                    color: f_s_r[0] === "2" ? "#0038c7":"#1aa7ff"
                    radius: 15
                }
                onClicked: {
                    python.write_plc("02")

                        }
            }
        }
    }
    Button {
        id: text_plc2
        x: 207
       y: 210
        width: 206
       height: 49
        text: "Conveyor2"
        font.pixelSize: size_conveyor
        background: Rectangle {
            color: "#7AA2AF"
            radius: 0
        }
    }
    Button {
        id: text_plc1
        x: 0
        y: 210
        width: 203
        height: 49
        text: "Conveyor1"
        font.pixelSize: size_conveyor
        background: Rectangle {
            color: "#7AA2AF"
            radius: 0
        }
    }
    Timer {
        interval: 25; running: true; repeat: true

        onTriggered: {
            f_s_r = python.get_plc_loop()
        }
    }

}
