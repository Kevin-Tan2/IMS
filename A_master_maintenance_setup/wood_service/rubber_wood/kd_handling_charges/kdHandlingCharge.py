import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import MasterMaintenance


class KDHandlingCharges(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "kdHandlingCharges.ui"
        self.csvFilePath = currentDir + "kdHandlingCharges.csv"

        # create headers for .csv use
        self.columnNames = ['Customer ID', 'Handling Charges', 'Type']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = KDHandlingCharges()
    widget.show()
    sys.exit(app.exec_())