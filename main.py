import sys

from PyQt5.QtCore import QAbstractTableModel, QPropertyAnimation
from login import login
from customer_entry import customerEntry_proto
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from tableViewModel import tableModel, load_csv
import pandas as pd
import icons
from pathlib import Path


class MasterMaintenance(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        # load the main.ui

        loadUi("main.ui", self)

        # side bar menu animation
        self.animation = QPropertyAnimation(self.sideMenuContainer, b"maximumWidth")  # Animate minimumWidht

        # set event responses
        self.customerEntryBtn.clicked.connect(lambda: self.display(0))
        self.rwContBtn.clicked.connect(lambda: self.display(1))
        self.rwSupplierBtn.clicked.connect(lambda: self.display(2))
        self.userMaintBtn.clicked.connect(lambda: self.display(3))
        self.kdChargeBtn.clicked.connect(lambda: self.display(4))
        self.ptChargeBtn.clicked.connect(lambda: self.display(5))
        self.contPriceOneBtn.clicked.connect(lambda: self.display(6))
        self.contPriceTwoBtn.clicked.connect(lambda: self.display(7))
        self.contPriceFJBtn.clicked.connect(lambda: self.display(8))
        self.fwContChargeBtn.clicked.connect(lambda: self.display(9))
        self.rwChargeDurationBtn.clicked.connect(lambda: self.display(10))
        self.fwrwSpeciesBtn.clicked.connect(lambda: self.display(11))

        # set event response for side bar menu button
        self.sideMenuBtn.clicked.connect(self.toggleMenu)

    def display(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def toggleMenu(self):
        # Get current left menu width
        width = self.sideMenuContainer.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 228
        # If maximized
        else:
            # Restore menu
            newWidth = 0

        # Animate the transition
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


class Controller:

    def __init__(self):
        self.masterMaintenance = MasterMaintenance()
        self.loginPage = login.LoginPage("./login/login.ui", "./login/listUsers.csv")

    def show_login(self):
        # display login page
        self.loginPage.show()

        # event response when the signal is emitted from the login page
        self.loginPage.switch_window.connect(self.show_maintenance)

    def show_maintenance(self):
        # close the login page
        self.loginPage.close()

        # display the customer entry
        self.masterMaintenance.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
