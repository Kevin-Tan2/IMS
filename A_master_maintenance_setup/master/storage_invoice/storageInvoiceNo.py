import sys

from PyQt5 import QtWidgets

from masterMaintenance import InvoiceWidget
import pandas as pd


class StorageInvoice(InvoiceWidget):

    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "storageInvoiceNo.ui"
        self.csvFilePath = currentDir + "storageInvoiceList.csv"

        self.columnNames = ['Invoice No']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def construct_df(self):
        df = pd.DataFrame({'Invoice No': [str(self.inputNo.text())]})
        return df

    def refresh_input_text(self):
        if not self.df.empty:
            self.inputNo.setText(str(self.df['Invoice No'].iloc[-1]))


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = StorageInvoice()
    widget.show()
    sys.exit(app.exec_())
