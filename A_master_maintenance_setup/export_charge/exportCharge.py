import sys
from typing import Union

import icons_rc
from PyQt5.QtCore import QPropertyAnimation, QPoint, Qt
from PyQt5.QtWidgets import QVBoxLayout, QSizeGrip
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from A_master_maintenance_setup.export_charge.freight_charges.freightCharges import FreightCharges
from A_master_maintenance_setup.export_charge.charges_by_size.sizeCharges import SizeCharge
from A_master_maintenance_setup.export_charge.export_no.exportInvoice import ExportInvoice

# Global value for the windows status
WINDOW_SIZE = 0


class ExportCharge(QtWidgets.QMainWindow):

    def __init__(self, currentDir=None):

        super().__init__()

        uiFilePath = "exportCharge.ui"

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

    def init_stacked_widget(self, currentDir=""):
        self.A23 = FreightCharges(currentDir + "freight_charges")
        self.stackedWidget.addWidget(self.A23)
        self.A24 = SizeCharge(currentDir + "charges_by_size")
        self.stackedWidget.addWidget(self.A24)
        self.A25 = ExportInvoice(currentDir + "export_no")
        self.stackedWidget.addWidget(self.A25)

        self.stackedWidget.setCurrentIndex(0)

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
    widget = ExportCharge()
    widget.show()
    sys.exit(app.exec_())
