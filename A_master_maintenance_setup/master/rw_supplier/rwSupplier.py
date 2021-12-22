import sys
from PyQt5 import QtWidgets, QtCore
from masterMaintenance import MasterMaintenance
from tableViewModel import tableModel, load_csv
import pandas as pd


class RWSupplier(MasterMaintenance):

    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "rwSupplier.ui"
        self.csvFilePath = currentDir + "rwSupplierList.csv"

        # create headers for .csv use
        self.columnNames = ['Supplier ID', 'Supplier Name']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        self.supplierID.clear()
        self.supplierName.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        supplierName = str(self.supplierName.text())
        supplierID = str(self.supplierID.text())

        df = pd.DataFrame({'Supplier ID': [supplierID],
                           'Supplier Name': [supplierName]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = RWSupplier()
    widget.show()
    sys.exit(app.exec_())
