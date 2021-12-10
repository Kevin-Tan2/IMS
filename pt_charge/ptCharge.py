import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
from tableViewModel import tableModel, load_csv
import os.path
from pathlib import Path


class PTCharge(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        uiFilePath = "./pt_charge/ptCharge.ui"
        csvFilePath = "./pt_charge/ptChargeList.csv"

        # load the ui file
        loadUi(uiFilePath, self)

        # load the csv file as dataframe
        self._columnNames = ['Customer ID', 'Price']
        self._df = load_csv(csvFilePath, self._columnNames)
        self._df = self._df.sort_values('Customer ID')

        # table model
        self._model = tableModel(self._df)

        # table view model
        self.tableView.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.tableView.setModel(self._model)  # to set the proxy model into the table view


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    testWidget = PTCharge()
    testWidget.show()
    sys.exit(app.exec_())