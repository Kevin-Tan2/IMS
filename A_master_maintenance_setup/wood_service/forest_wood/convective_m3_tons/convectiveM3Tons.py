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


class ConvectiveM3Tons(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "convectiveM3Tons.ui"
        self.csvFilePath = currentDir + "convectiveM3Tons.csv"

        # create headers for .csv use
        self.columnNames = ['M3', 'Tons']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clear out the entries
        self.metric.clear()
        self.tons.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        metric = str(self.metric.text())
        tons = str(self.tons.text())

        df = pd.DataFrame({'M3': [metric],
                           'Tons': [tons]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = ConvectiveM3Tons()
    widget.show()
    sys.exit(app.exec_())
