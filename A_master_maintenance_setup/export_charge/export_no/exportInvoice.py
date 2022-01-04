import sys
from PyQt5 import QtWidgets
import pandas as pd
from masterMaintenance import InvoiceWidget


class ExportInvoice(InvoiceWidget):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "exportInvoice.ui"
        self.csvFilePath = currentDir + "exportInvoice.csv"

        # create headers for .csv use
        self.columnNames = ['Invoice No']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def construct_df(self):
        df = pd.DataFrame({'Invoice No': [str(self.inputNo.text())]})
        return df


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = ExportInvoice()
    widget.show()
    sys.exit(app.exec_())
