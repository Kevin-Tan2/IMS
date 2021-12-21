import sys
import os
from PyQt5.QtCore import QPropertyAnimation
from login import login
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from A_master_maintenance_setup.master.storage_invoice.storageInvoiceNo import StorageInvoice
from A_master_maintenance_setup.master.fw_cancel_no.fwCancelNo import FWCancel


class Master(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        # to create separate window for Storage Invoice
        self.storageInvoice = StorageInvoice()
        self.cancelStock = FWCancel()

        # load the master.ui
        loadUi("master.ui", self)

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
