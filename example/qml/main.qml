import QtQuick
import QtQuick.Controls

import testclass

ApplicationWindow {

    id: root

    visible: true
    width: 640
    height: 480

    Component.onCompleted: {
        console.log("ApplicationWindow.onCompleted");
    }

    TestClass{
        p0:"123456"
        p1:123456
        p2:123456.123456
    }

}