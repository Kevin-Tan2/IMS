import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import MasterMaintenance
from tableViewModel import tableModel, load_csv


class LorryTransportCharges(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "lorryTransportCharges.ui"
        self.csvFilePath = currentDir + "lorryTransportCharges.csv"

        # create headers for .csv use
        self.columnNames = ['Customer ID', 'Lorry No', 'Price', 'Type']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clear out the entries
        self.customerID.clear()
        self.lorryNo.clear()
        self.price.clear()


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = LorryTransportCharges()
    widget.show()
    sys.exit(app.exec_())
