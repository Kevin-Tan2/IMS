import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi


class MasterMaintenanceSetup(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, currentDir=None):
        super().__init__()

        if currentDir is None:
            uiFilePath = "masterMaintenanceSetup.ui"

        else:
            uiFilePath = currentDir + "/masterMaintenanceSetup.ui"

        # load ui
        loadUi(uiFilePath, self)

        self.masterMaintenance = None

        self.dropBox.activated.connect(self.switch_widget)
        self.closeButton.clicked.connect(self.back)

    def switch_widget(self):
        self.stackedWidget.setCurrentIndex(self.dropBox.currentIndex())

    def back(self):
        self.switch_window.emit()
        self.close()

