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

    def reset_entries(self):
        # clear out the entries
        self.customerID.clear()
        self.handlingCharges.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        customerID = str(self.customerID.text())
        handlingCharges = str(self.handlingCharges.text())

        handlingType = None

        if self.tonBtn.isChecked():
            handlingType = str(self.tonBtn.text())

        elif self.tripBtn.isChecked():
            handlingType = str(self.tripBtn.text())

        df = pd.DataFrame({'Customer ID': [customerID],
                           'Handling Charges': [handlingCharges],
                           'Type': [handlingType]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = KDHandlingCharges()
    widget.show()
    sys.exit(app.exec_())