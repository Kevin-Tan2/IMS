import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import InvoiceWidget


class RWSerialNo(InvoiceWidget):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "rwSerialNo.ui"
        self.csvFilePath = currentDir + "rwSerialNo.csv"

        # create headers for .csv use
        self.columnNames = ['SerialNo']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = RWSerialNo()
    widget.show()
    sys.exit(app.exec_())
