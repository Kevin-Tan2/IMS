import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
import os.path
from pathlib import Path

from main import load_csv, tableModel


class RWSupplier(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        uiFilePath = "./rw_supplier/rwSupplier.ui"
        csvFilePath = "./rw_supplier/rwSupplierList.csv"

        # load ui file
        loadUi(uiFilePath, self)

        # create headers for .csv use
        self._columnNames = ['Supplier ID', 'Supplier Name']

        # load contractorList.csv
        self._df = load_csv(csvFilePath, self._columnNames)

        # create tableModel instance
        self._model = tableModel(self._df)

        # table view model
        self.tableView.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.tableView.setModel(self._model)  # to set the proxy model into the table view

        # set event
        self.resetButton.clicked.connect(self.reset_entries)
        self.addButton.clicked.connect(self.add_df)
        self.deleteButton.clicked.connect(self.delete_row)

    def reset_entries(self):
        self.supplierID.clear()
        self.supplierName.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        supplierName = str(self.supplierName.text())
        supplierID = str(self.supplierID.text())

        df = pd.DataFrame({'Supplier ID': [supplierName],
                           'Supplier Name': [supplierID]})
        return df

    def refresh_table(self):
        # refresh the table whenever data frame has been changed
        self._model = tableModel(self._df)
        self.tableView.setModel(self._model)

    def add_df(self):
        # adding new data into the dataframe
        df1 = self._df  # store the current data frame into a temp variable
        df2 = self.construct_df()
        self._df = df1.append(df2, ignore_index=True)  # adding new row into the dataframe
        self.refresh_table()

    def delete_row(self):
        # delete the selected row
        index_list = []  # to store list of selected rows

        for model_index in self.tableView.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)  # append the selected indices into index_list

        for index in index_list:  # delete all selected rows
            tempDf = self._df
            self._df = tempDf.drop(index.row())  # delete each selected row from the dataframe

        self._df = self._df.reset_index(drop=True)  # reset the index in numerical order
        self.refresh_table()
