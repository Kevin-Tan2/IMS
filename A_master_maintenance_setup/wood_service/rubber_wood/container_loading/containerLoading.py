import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import MasterMaintenance


class ContainerLoading(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "containerLoading.ui"
        self.csvFilePath = currentDir + "containerLoading.csv"

        # create headers for .csv use
        self.columnNames = ['Customer ID', 'Container Charges', 'Type']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clear out the entries
        self.customerID.clear()
        self.containerCharges.clear()


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = ContainerLoading()
    widget.show()
    sys.exit(app.exec_())