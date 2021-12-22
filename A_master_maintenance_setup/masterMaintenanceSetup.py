import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from master.master import Master


class MasterMaintenanceSetup(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, currentDir=None):
        super().__init__()

        uiFilePath = "masterMaintenanceSetup.ui"

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        uiFilePath = currentDir + uiFilePath

        # load ui
        loadUi(uiFilePath, self)

        self.masterMaintenance = Master(currentDir + "master")

        self.dropBox.activated.connect(self.switch_widget)
        self.closeButton.clicked.connect(self.back)
        self.customerEntryBtn.clicked.connect(lambda: self.enter_widget(0))

    def switch_widget(self):
        self.stackedWidget.setCurrentIndex(self.dropBox.currentIndex())

    def back(self):
        self.switch_window.emit()
        self.close()

    def enter_widget(self, index):
        self.masterMaintenance.show()


# Create main function to test the module individually
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    masterSetup = MasterMaintenanceSetup()
    masterSetup.show()
    sys.exit(app.exec_())
