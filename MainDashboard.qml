import QtQuick 2.15

Item {
    id: main_dashboard

    Image {
        id: dashBackground
        source: "images/TableroMontse.png"
        anchors.centerIn: parent

        Text{
            text: "Mensaje de CAN"
            anchors.centerIn:parent
            color: "white"
        }
    }


}
