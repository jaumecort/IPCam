import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12
import QtQuick.Window 2.15
import Qt.labs.folderlistmodel 
//import "C:/TFG/untitled/OnvifPtzController.py" as Controller


Window {
    id: main_window
    visible: true
    width: 400
    height: 300
    title: "Control PTZ"


    ColumnLayout {
        anchors.centerIn: parent

        Button {
            text: "Mover a la derecha"
            onClicked: onvif_controller.move(self, 1.0, 0.0, 0.0)
        }

        Button {
            text: "Mover a la izquierda"
            onClicked: onvif_controller.move(-1.0, 0.0, 0.0)
        }

        Button {
            text: "Mover hacia arriba"
            onClicked: onvif_controller.move(0.0, 1.0, 0.0)
        }

        Button {
            text: "Mover hacia abajo"
            onClicked: onvif_controller.move(0.0, -1.0, 0.0)
        }

        Button {
            text: "Detener movimiento"
            onClicked: onvif_controller.stop()
        }
    }
}
