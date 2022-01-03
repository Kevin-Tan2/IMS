import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import MasterMaintenance


class FJKDCharge(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "fjKDCharge.ui"
        self.csvFilePath = currentDir + "fjKDCharge.csv"

        # create headers for .csv use
        self.columnNames = ['Customer ID', 'Size 1', 'Size 2', 'Price']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clear out the entries
        self.customerID.clear()
        self.size1.clear()
        self.size2.clear()
        self.price.clear()


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = FJKDCharge()
    widget.show()
    sys.exit(app.exec_())