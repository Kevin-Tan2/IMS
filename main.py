import sys

from PyQt5.QtCore import QPropertyAnimation
from login import login
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from tableViewModel import load_csv, tableModel
from storage_invoice.storageInvoiceNo import StorageInvoice
from fw_cancel_no.fwCancelNo import FWCancel


class MasterMaintenance(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        # to create separate window for Storage Invoice
        self.storageInvoice = StorageInvoice()
        self.cancelStock = FWCancel()

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
        self.contPriceOneBtn.clicked.connect(lambda: self.display(7))
        self.contPriceTwoBtn.clicked.connect(lambda: self.display(8))
        self.contPriceFJBtn.clicked.connect(lambda: self.display(9))
        self.fwContChargeBtn.clicked.connect(lambda: self.display(10))
        self.rwChargeDurationBtn.clicked.connect(lambda: self.display(11))
        self.fwrwSpeciesBtn.clicked.connect(lambda: self.display(12))
        self.stockInvoiceBtn.clicked.connect(self.display_invoice)
        self.fwCancelNoBtn.clicked.connect(self.cancelStock.show)
        # set event response for side bar menu button
        self.sideMenuBtn.clicked.connect(self.toggleMenu)

    def display_invoice(self):
        self.storageInvoice.show()

    def display(self, index):
        self.stackedWidget.setCurrentIndex(index)
        self.stackedTitle.setCurrentIndex(index)

    def toggleMenu(self):
        # Get current left menu width
        width = self.sideMenuContainer.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 240
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
