import sys
from typing import Union

import icons_rc
from PyQt5.QtCore import QPropertyAnimation, QPoint, Qt
from PyQt5.QtWidgets import QVBoxLayout, QSizeGrip
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from A_master_maintenance_setup.wood_service.forest_wood.convective_m3_tons.convectiveM3Tons import ConvectiveM3Tons
from A_master_maintenance_setup.wood_service.forest_wood.fw_serial_no.fwSerialNo import FWSerialNo
from A_master_maintenance_setup.wood_service.forest_wood.invoice_no.invoiceNo import InvoiceNo
from A_master_maintenance_setup.wood_service.forest_wood.lorry_transport.lorryTransportCharges import \
    LorryTransportCharges

from A_master_maintenance_setup.wood_service.rubber_wood.fj_kd_charge.fjKDCharge import FJKDCharge
from A_master_maintenance_setup.wood_service.rubber_wood.kd_handling_charges.kdHandlingCharge import KDHandlingCharges
from A_master_maintenance_setup.wood_service.rubber_wood.rw_serial_no.rwSerialNo import RWSerialNo
from A_master_maintenance_setup.wood_service.rubber_wood.container_loading.containerLoading import ContainerLoading

# Global value for the windows status
WINDOW_SIZE = 0


class WoodService(QtWidgets.QMainWindow):

    def __init__(self, currentDir=None):

        super().__init__()

        uiFilePath = "woodService.ui"

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + uiFilePath
        self.currentDir = currentDir

        # load the master.ui
        loadUi(self.uiFilePath, self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # to remove the default window frame
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # to give transparent background (provide round corners)
        self.oldPos = self.pos()

        # header's property
        self.closeBtn.clicked.connect(lambda: self.close())
        self.maxBtn.clicked.connect(lambda: self.toggle_max_restore())
        self.minBtn.clicked.connect(lambda: self.showMinimized())
        self.header.mouseMoveEvent = self.moveWindow

        # side menu event
        self.animation = QPropertyAnimation(self.sideMenuContainer, b"minimumWidth")  # Animate minimumWidht
        self.sideMenuBtn.clicked.connect(lambda: self.slideLeftMenu())

        # added QSizeGrip to make the window resizeable
        QSizeGrip(self.sizeGripCorner)
        self.sizeGripX.setCursor(QtCore.Qt.SizeHorCursor)
        self.sizeGripX.mouseMoveEvent = self.resizeRight
        self.sizeGripY.setCursor(QtCore.Qt.SizeVerCursor)
        self.sizeGripY.mouseMoveEvent = self.resizeBottom

        # add stacked widgets
        self.init_stacked_widget(currentDir)

        # hide the tree widget
        self.treeWidget.hide()
        self.treeWidget.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item, column):
        index = 0
        if item.text(column) == "A15 Invoice No":
            index = 0
        elif item.text(column) == "A16 Forest Wood DO No":
            index = 1
        elif item.text(column) == "A17 Lorry Transport":
            index = 2
        elif item.text(column) == "A18 Convective M3 Tons":
            index = 3
        elif item.text(column) == "A19 Finger joined KD Charge":
            index = 4
        elif item.text(column) == "A20 KD Handling Charges Master Data Entry":
            index = 5
        elif item.text(column) == "A21 Rubber Wood DO No":
            index = 6
        elif item.text(column) == "A22 Container Loading Charges Master Data Entry":
            index = 7
        else:
            return
        self.display_widget(index)

    def display_widget(self, index):
        # display widgets according to the selected tree widget item
        self.stackedWidget.setCurrentIndex(index)

    def init_stacked_widget(self, currentDir=""):
        self.A15 = InvoiceNo(currentDir + "forest_wood/invoice_no")
        self.stackedWidget.addWidget(self.A15)
        self.A16 = FWSerialNo(currentDir + "forest_wood/fw_serial_no")
        self.stackedWidget.addWidget(self.A16)
        self.A17 = LorryTransportCharges(currentDir + "forest_wood/lorry_transport")
        self.stackedWidget.addWidget(self.A17)
        self.A18 = ConvectiveM3Tons(currentDir + "forest_wood/convective_m3_tons")
        self.stackedWidget.addWidget(self.A18)

        self.A19 = FJKDCharge(currentDir + "rubber_wood/fj_kd_charge")
        self.stackedWidget.addWidget(self.A19)
        self.A20 = KDHandlingCharges(currentDir + "rubber_wood/kd_handling_charges")
        self.stackedWidget.addWidget(self.A20)
        self.A21 = RWSerialNo(currentDir + "rubber_wood/rw_serial_no")
        self.stackedWidget.addWidget(self.A21)
        self.A22 = ContainerLoading(currentDir + "rubber_wood/container_loading")
        self.stackedWidget.addWidget(self.A22)

        self.stackedWidget.setCurrentIndex(1)

    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.oldPos = event.globalPos()

    def moveWindow(self, event):
        # if left mouse button is clicked (Only accept left mouse button clicks)
        if event.buttons() == Qt.LeftButton:
            # Move window
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    # Restore or maximize your window
    def toggle_max_restore(self):
        # Global windows state
        global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            self.showMaximized()

        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been set to normal size
            self.showNormal()

    # Toggle side menu bar
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.sideMenuContainer.width()

        # If minimized
        if width == 60:
            # Expand menu
            newWidth = 300
            self.treeWidget.show()
        # If maximized
        else:
            # Restore menu
            newWidth = 60
            self.treeWidget.hide()

        # Animate the transition
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # resize window right and bottom
    def resizeRight(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        width = max(self.minimumWidth(), self.width() + delta.x())
        self.resize(width, self.height())
        self.oldPos = event.globalPos()

    def resizeBottom(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        height = max(self.minimumHeight(), self.height() + delta.y())
        self.resize(self.width(), height)
        self.oldPos = event.globalPos()


# Create main function to test the module individually
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = WoodService()
    widget.show()
    sys.exit(app.exec_())
