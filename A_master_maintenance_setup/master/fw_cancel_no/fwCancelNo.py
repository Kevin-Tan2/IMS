import sys

from PyQt5 import QtWidgets

from masterMaintenance import InvoiceWidget
import pandas as pd


class FWCancel(InvoiceWidget):

    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "fwCancelNo.ui"
        self.csvFilePath = currentDir + "fwCancelList.csv"
        self.columnNames = ['Cancel No']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def construct_df(self):
        df = pd.DataFrame({'Cancel No': [str(self.inputNo.text())]})
        return df

    def refresh_input_text(self):
        if not self.df.empty:
            self.inputNo.setText(str(self.df['Cancel No'].iloc[-1]))


# to test the module individually
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    customerEntry = FWCancel()
    customerEntry.show()
    sys.exit(app.exec_())