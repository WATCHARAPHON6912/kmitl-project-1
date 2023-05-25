// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0

import QtQuick 6.4
import QtQuick.Controls.Material
import QtQuick.Controls 6.4
import "../imports/UntitledProject"


//ApplicationWindow {
Window {
    id:win
    width: 1530
    height: 780
    property bool closing: false
    property  color button_text_color: "#000000"


//    onClosing: {

//        close.accepted = closing
//        onTriggered:{
//            if(status_m1 === false && status_plc===false && status_camera === false){
//                closing = true
//                win.close()
//            }else{
//                myImageProvider.no_exit()
//            }


//        }

//    }


//    width: 500
//    height: 250


    visible: true
    title: "Project"
    property double app_joint1: 400
    property double app_joint2: 90
    property double app_joint3: 90
    property double app_joint4: 90
    property double show_joint1: 230
    property double show_joint2: 0
    property double show_joint3: 0
    property double show_joint4: 0
    property int size: 13
    property int button_h: 70
    property int button_w: 70
    property bool status_m1: false
    property bool status_plc: false
    property bool status_camera: false
    property bool con: false




    Screen01 {
        Material.theme: mode.checked ? Material.Dark:Material.Light
        id: mainScreen
        sc_joint1: app_joint1
        sc_joint2: app_joint2
        sc_joint3: app_joint3
        view3d_color:mode.checked ? "#000000":"#d9d9d9"
        x: 0
        y: 0

        Switch {
            id :mode
            x: 5
            y: 116
            width: 248
            height: 48
            text: mode.checked ? "Light Mode":"Dark Mode"
        }
        Switch {
            id :mode_j
            x: 246
            y: 495
            width: 215
            height: 48
            text:mode_j.checked ? "X Y Z R":"Joint"
        }

        Text {
            id: j1
            x: 255
            y: 552
            width: 202
            height: 31
            text: "j1 = "+show_joint1
            color:mode.checked ?  "#ffffff":"#000000"
            font.pixelSize: 25
        }
        Text {
            id: j2
            x: 255
            y: 582
            width: 202
            height: 37
            text: "j2 = "+show_joint2
            color:mode.checked ?  "#ffffff":"#000000"
            font.pixelSize: 25
        }

        Text {
            id: j3
            x: 252
            y: 617
            width: 202
            height: 43
            color: mode.checked ?  "#ffffff":"#000000"
            text: "j3 = "+show_joint3
            font.pixelSize: 25
        }
        Text {
            id: j4
            x: 253
            y: 651
            width: 202
            height: 43
            color: mode.checked ?  "#ffffff":"#000000"
            text: "j4 = "+show_joint4
            font.pixelSize: 25
            
        }

        Button {
            id: button_j1_add
            enabled: con
            x: 62
            y: 484
            width: button_w
            height: button_h
            text: mode_j.checked ? "+X":"+J1"
            font.pixelSize: size
            contentItem: Text {
                    text:button_j1_add.text
                    font: button_j1_add.font
                    opacity: enabled ? 1.0 : 0.3
                    color: button_text_color
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
            background: Rectangle {
                radius: 70
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
            }
        }

        Button {
            id: button_j1_sub
            enabled: con
            x: 62
            y: 553
            width: button_w
            height: button_h
            text: mode_j.checked ?  "-X":"-J1"
            font.pixelSize: size
            contentItem: Text {
                    text:button_j1_sub.text
                    font: button_j1_sub.font
                    opacity: enabled ? 1.0 : 0.3
                    color: button_text_color
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
            background: Rectangle {
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
                radius: 70
            }
        }

        Button {
            id: button_j2_add
            enabled: con
            x: 0
            y: 518
            width: button_w
            height: button_h
            text: mode_j.checked ? "+Y":"+J2"
            font.pixelSize: size
            contentItem: Text {
                    text:button_j2_add.text
                    font: button_j2_add.font
                    opacity: enabled ? 1.0 : 0.3
                    color: button_text_color
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
            background: Rectangle {
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
                radius: 70
            }
        }

        Button {
            id: button_j2_sub
            enabled: con
            x: 125
            y: 518
            width: button_w
            height: button_h
            text: mode_j.checked ? "-Y":"-J2"
            font.pixelSize: size
            contentItem: Text {
                    text:button_j2_sub.text
                    font: button_j2_sub.font
                    opacity: enabled ? 1.0 : 0.3
                    color: button_text_color
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
            background: Rectangle {
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
                radius: 70
            }
        }

        Button {
            id: button_j3_add
            enabled: con
            x: 62
            y: 618
            width: button_w
            height: button_h
            text: mode_j.checked ? "+Z":"+J3"
            font.pixelSize: size
            contentItem: Text {
                    text:button_j3_add.text
                    font: button_j3_add.font
                    opacity: enabled ? 1.0 : 0.3
                    color: button_text_color
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
            background: Rectangle {
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
                radius: 70
            }
        }

        Button {
            id: button_j3_sub
            enabled: con
            x: 62
            y: 687
            width: button_w
            height: button_h
            text: mode_j.checked ? "-Z":"-J3"
            font.pixelSize: size
            contentItem: Text {
                    text:button_j3_sub.text
                    font: button_j3_sub.font
                    opacity: enabled ? 1.0 : 0.3
                    color: button_text_color
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
            background: Rectangle {
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
                radius: 70
            }
        }

        Button {
            id: button_j4_add
            enabled: con
            x: 0
            y: 651
            width: button_w
            height: button_h
            text: mode_j.checked ? "+R":"+J4"
            font.pixelSize: size
            contentItem: Text {
                    text:button_j4_add.text
                    font: button_j4_add.font
                    opacity: enabled ? 1.0 : 0.3
                    color: button_text_color
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
            background: Rectangle {
                color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
                radius: 70
            }
            
        }

        Button {
            id: button_j4_sub
            enabled: con
            x: 125
            y: 652
            width: button_w
            height: button_h
           text: mode_j.checked ? "-R":"-J4"
           font.pixelSize: size
           contentItem: Text {
                   text:button_j4_sub.text
                   font: button_j4_sub.font
                   opacity: enabled ? 1.0 : 0.3
                   color: button_text_color
                   horizontalAlignment: Text.AlignHCenter
                   verticalAlignment: Text.AlignVCenter
                   elide: Text.ElideRight
               }
           background: Rectangle {
               color: parent.down ? "#0b2042" : (parent.hovered ? "#12b3aa" : "#aeb312")
               radius: 70
           }

        }
        Text {
            id: text1
            x: 1076
            y: 560
            width: 403
            height: 59
            text: qsTr("Camera not connected")
            font.pixelSize: 40
            color: mode.checked ? "#ffffff":"000000"
        }

        Image {
               id: feedImage
               width: 459
               height: 337
//               fillMode: Image.PreserveAspectFit
               cache: false
               source: "image.jpg"
               property bool counter: false
               x: 1047
               y: 414


               function reloadImage() {
                   counter = !counter
                   source = "image://MyImageProvider/img?id=" + counter
               }
           }

        Connections{
                target: myImageProvider

                function onImageChanged(image) {
                    //                    console.log("emit")
                    feedImage.reloadImage()
                }
        }

            Switch {
                id: mode_m1
                x: 213
                y: 116
                width: 248
                height: 48
                text:mode_m1.checked ? "Manual":"Auto"
            }
    }

    Connect_input{
        scale: 1
        color_text: mode.checked ? "#ffffff":"#000000"
        textinput_color:mode.checked ? "#000000":"#66ffff"
    }
    Show_number{
        mode_color:  mode.checked ? "#3e6869":"#80D8EE"
        text_color:  mode.checked ? "#ff0000":"000000"
    }
    Plc_control{
        text_color: mode.checked ? "#ffffff":"000000"

    }
    function map(x, in_min, in_max, out_min, out_max){

            return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min).toFixed(2);
        }
    Timer {
        interval: 25; running: true; repeat: true

        onTriggered: {
        app_joint1 = python.joint1_loop()
        app_joint2 = python.joint2_loop()
        app_joint3 = python.joint3_loop()
        app_joint4 = python.joint4_loop()

        show_joint1 = map(app_joint1,100,400,15,230)
        show_joint2 = map(app_joint2,0,180,-80,90)
        show_joint3 = map(app_joint3,-50,230,-130,130)
        show_joint4 = map(app_joint4,-50,230,-130,130)
        status_m1 = python.return_m1()

//        console.log()
        if(status_m1 == true && (mode_m1.checked ? "Auto":"Manual")==="Manual"){
            con = true
        }else{
            con = false
        }
        // console.log(con)
        python.mode_m1(con)

        status_plc = python.return_plc()
        status_camera =python.return_camera()
//        python.mode_m1(mode_m1.clicked ? "0":"1")

        if (button_j1_add.down){python.send(mode_j.checked ? "+X":"+J1")}
        if (button_j1_sub.down){python.send(mode_j.checked ? "-X":"-J1")}
        if (button_j2_add.down){python.send(mode_j.checked ? "+Y":"+J2")}
        if (button_j2_sub.down){python.send(mode_j.checked ? "-Y":"-J2")}

        if (button_j3_add.down){python.send(mode_j.checked ? "+Z":"+J3")}
        if (button_j3_sub.down){python.send(mode_j.checked ? "-Z":"-J3")}
        if (button_j4_add.down){python.send(mode_j.checked ? "+R":"+J4")}
        if (button_j4_sub.down){python.send(mode_j.checked ? "-R":"-J4")}



        }
    }




}


