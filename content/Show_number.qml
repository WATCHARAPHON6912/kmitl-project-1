import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt.labs.qmlmodels 1.0
Rectangle{
    width: 1530
    height: 780
    color: "transparent"
    property color mode_color: "#80D8EE"
    property color text_color: "#000000"
    property color  color_title_reject: "#ffff00"
    property color  color_title_accept: "#00ff00"



//    property variant myStringList: [1,2,3,4]
//    property list<string> stringList: ["Apple", "Banana", "Cherry", "Durian"]

//    var myString = "apple banana cherry"
//    var myList = myString.split(" ")
//    var ggb = ["j","j"];


    ListModel {
        id: myListModel
        ListElement { name: "f" }
        ListElement { name: "f" }
        ListElement { name: "d" }
    }
    Rectangle{
        x: 750
        y: 40
        width: 300
        height: 780
        color: mode_color
        ListView {
            id: listView
            x: 0
            y: 0
            width: 300
            height: 740
            model:  stringListModel

            ScrollBar.vertical: ScrollBar {
                id: scrollBar
                active: listView.__scrollBarVisible
                size: listView.visibleArea.heightRatio
                position: listView.visibleArea.positionRatio
//                onPositionChanged: listView.positionViewAt(position)
            }

            delegate: Rectangle {
                width: listView.width
                height: 40
                color: mode.checked ? index % 2 == 0 ? "#677174" : "#698853":index % 2 == 0 ? "lightblue" : "lightgray"
                border.color: "white"
                border.width: 2
                Text {
                    anchors.centerIn: parent
                    text: model.display
                }
            }
        }

    }
    Rectangle{
        x: 420
        y: 40
        width: 300
        height: 780
        color: mode_color
        ListView {
            id: listView1
            x: 0
            y: 0
            width: 300
            height: 740
            model: stringListModel1

            ScrollBar.vertical: ScrollBar {
                id: scrollBar1
                active: listView1.__scrollBarVisible
                size: listView1.visibleArea.heightRatio
                position: listView1.visibleArea.positionRatio
//                onPositionChanged: listView1.positionViewAt(position)
            }

            delegate: Rectangle {
                width: listView1.width
                height: 40
                color: mode.checked ? index % 2 == 0 ? "#677174" : "#888253":index % 2 == 0 ? "lightblue" : "lightgray"
                border.color: "white"
                border.width: 2
                Text {
                    anchors.centerIn: parent
                    text: model.display
                }
            }
        }
    }
    Rectangle {
        x: 750
        y: 0
        color: color_title_accept
        width: 300
        height: 41
    Text {
        id: text_accept
        x: 0
        y: 0
        width: 300
        height: 41
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        text: qsTr("Accept")
        font.pixelSize: 30
    }
    }
    Rectangle {
        x: 420
        y: 0
        color: color_title_reject
        width: 300
        height: 41
        Text {
            id: text_reject
            x: 0
            y: 0
            width: 300
            height: 41
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            text: qsTr("Reject")
            font.pixelSize: 30
        }


    }
    Timer {
        interval: 1; running: true; repeat: true
        onTriggered: {
            //console.log(myImageProvider.get_runcard_on())
            stringListModel.addString(myImageProvider.get_runcard_on())
            //console.log(myImageProvider.get_reject_runcard_on())
            stringListModel1.addString(myImageProvider.get_reject_runcard_on())

            python.send_re_ac(myImageProvider.get_ac_re())
        }

    }




}
