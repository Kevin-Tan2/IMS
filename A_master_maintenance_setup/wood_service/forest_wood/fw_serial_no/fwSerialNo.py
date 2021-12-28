import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
from tableViewModel import tableModel, load_csv
from masterMaintenance import InvoiceWidget
import os.path
from pathlib import Path


class FWSerialNo(InvoiceWidget):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "fwSerialNo.ui"
        self.csvFilePath = currentDir + "fwSerialNo.csv"

        # create headers for .csv use
        self.columnNames = ['SerialNo']

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
    widget = FWSerialNo()
    widget.show()
    sys.exit(app.exec_())
