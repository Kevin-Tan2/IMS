import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import MasterMaintenance


class FreightCharges(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "freightCharges.ui"
        self.csvFilePath = currentDir + "freightCharges.csv"

        # create headers for .csv use
        self.columnNames = ['Port of Discharge', 'Freight Charges']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = FreightCharges()
    widget.show()
    sys.exit(app.exec_())
