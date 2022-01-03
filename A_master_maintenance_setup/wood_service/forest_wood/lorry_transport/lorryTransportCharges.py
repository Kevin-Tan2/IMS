import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import MasterMaintenance


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

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        customerID = str(self.customerID.text())
        lorryNo = str(self.lorryNo.text())
        price = str(self.price.text())
        woodType = None

        if self.tonnageBtn.isChecked():
            woodType = str(self.tonnageBtn.text())

        elif self.tripBtn.isChecked():
            woodType = str(self.tripBtn.text())

        df = pd.DataFrame({'Customer ID': [customerID],
                           'Lorry No': [lorryNo],
                           'Price': [price],
                           'Type': [woodType]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = LorryTransportCharges()
    widget.show()
    sys.exit(app.exec_())
