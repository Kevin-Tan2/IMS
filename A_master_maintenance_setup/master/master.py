import sys
import os
from PyQt5.QtCore import QPropertyAnimation
from login import login
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from .customer_entry.customerEntry import *
from .contractor_entry.contractorEntry import *
from .rw_supplier.rwSupplier import *
from .maintenance_entry.userMaintenanceEntry import *
from .kd_charge.kdCharge import *
from .pt_charge.ptCharge import *
from .contractor_price.contractorPriceOne import *
from .contractor_price.contractorPriceTwo import *
from .contractor_price.contractorPriceFJ import *
from .fw_contractor_charges.fwContCharges import *
from .rw_charge_duration.rwChargeDuration import *
from .fwrw_species.fwrwSpecies import *


class Master(QtWidgets.QMainWindow):

    def __init__(self, currentDir=None):

        super().__init__()

        uiFilePath = "master.ui"

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + uiFilePath
        self.currentDir = currentDir

        # load the master.ui
        loadUi(self.uiFilePath, self)

        self.init_stacked_widget(currentDir)

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
        self.sideMenuBtn.clicked.connect(self.toggleMenu)

    def init_stacked_widget(self, currentDir=""):
        self.A1 = CustomerEntry(currentDir + "customer_entry")
        self.stackedWidget.addWidget(self.A1)
        self.A2 = ContractorEntry(currentDir + "contractor_entry")
        self.stackedWidget.addWidget(self.A2)
        self.A3 = RWSupplier(currentDir + "rw_supplier")
        self.stackedWidget.addWidget(self.A3)
        self.A4 = UserMaintenance(currentDir + "maintenance_entry")
        self.stackedWidget.addWidget(self.A4)
        self.A5 = KDCharge(currentDir + "kd_charge")
        self.stackedWidget.addWidget(self.A5)
        self.A6 = PTCharge(currentDir + "pt_charge")
        self.stackedWidget.addWidget(self.A6)
        self.A7 = QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.A7)
        self.A8 = ContractorPriceOne(currentDir + "contractor_price")
        self.stackedWidget.addWidget(self.A8)
        self.A9 = ContractorPriceTwo(currentDir + "contractor_price")
        self.stackedWidget.addWidget(self.A9)
        self.A10 = ContractorPriceFJ(currentDir + "contractor_price")
        self.stackedWidget.addWidget(self.A10)
        self.A11 = FWContCharges(currentDir + "fw_contractor_charges")
        self.stackedWidget.addWidget(self.A11)
        self.A12 = RWChargeDuration(currentDir + "rw_charge_duration")
        self.stackedWidget.addWidget(self.A12)
        self.A13 = FWRWSpecies(currentDir + "fwrw_species")
        self.stackedWidget.addWidget(self.A13)

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


# Create main function to test the module individually
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Master()
    widget.show()
    sys.exit(app.exec_())
