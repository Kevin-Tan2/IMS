import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
from masterMaintenance import MasterMaintenance
import os.path
from pathlib import Path

from main import load_csv, tableModel


class RWSupplier(MasterMaintenance):

    def __init__(self):

        self.uiFilePath = "./rw_supplier/rwSupplier.ui"
        self.csvFilePath = "./rw_supplier/rwSupplierList.csv"

        # create headers for .csv use
        self.columnNames = ['Supplier ID', 'Supplier Name']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        self.supplierID.clear()
        self.supplierName.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        supplierName = str(self.supplierName.text())
        supplierID = str(self.supplierID.text())

        df = pd.DataFrame({'Supplier ID': [supplierID],
                           'Supplier Name': [supplierName]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)
