import sys
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets


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


# Create main function to test the module individually
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = WoodService()
    widget.show()
    sys.exit(app.exec_())