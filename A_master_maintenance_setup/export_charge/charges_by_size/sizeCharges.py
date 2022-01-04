import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import MasterMaintenance


class SizeCharge(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "sizeCharges.ui"
        self.csvFilePath = currentDir + "sizeCharges.csv"

        # create headers for .csv use
        self.columnNames = ['Customer ID', 'Size 1', 'Size 2', 'Price']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clear out the entries
        self.customerID.clear()
        self.sizeOne.clear()
        self.sizeTwo.clear()
        self.price.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        customerID = str(self.customerID.text())
        sizeOne = str(self.sizeOne.text())
        sizeTwo = str(self.sizeTwo.text())
        price = str(self.price.text())

        df = pd.DataFrame({'Customer ID': [customerID],
                           'Size 1': [sizeOne],
                           'Size 2': [sizeTwo],
                           'Price': [price]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = SizeCharge()
    widget.show()
    sys.exit(app.exec_())
