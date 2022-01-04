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

    def reset_entries(self):
        # clear out the entries
        self.dischargePort.clear()
        self.containerCharge.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        dischargePort = str(self.dischargePort.text())
        containerCharge = str(self.containerCharge.text())

        df = pd.DataFrame({'Port of Discharge': [dischargePort],
                           'Freight Charges': [containerCharge]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = FreightCharges()
    widget.show()
    sys.exit(app.exec_())
