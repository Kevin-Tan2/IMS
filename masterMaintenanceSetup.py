import sys

from PyQt5.QtCore import QPropertyAnimation
from login import login
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi


class MasterMaintenanceSetup(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("masterMaintenanceSetup.ui", self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    setup = MasterMaintenanceSetup()
    setup.show()
    sys.exit(app.exec_())
