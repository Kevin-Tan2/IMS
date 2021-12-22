import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
from tableViewModel import tableModel, load_csv
from masterMaintenance import MasterMaintenance
import os.path
from pathlib import Path


class PTCharge(MasterMaintenance):

    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "ptCharge.ui"
        self.csvFilePath = currentDir + "ptChargeList.csv"

        # load the csv file as dataframe
        self.columnNames = ['Customer ID', 'Price']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clears the line entries
        self.customerID.clear()
        self.price.clear()

    def construct_df(self):
        customerID = str(self.customerID.text())
        price = str(self.price.text())

        df = pd.DataFrame({'Customer ID': [customerID],
                           'Price': [price]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = PTCharge()
    widget.show()
    sys.exit(app.exec_())
