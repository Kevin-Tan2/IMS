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
        # adding new data into the dataframe
        df1 = self.df  # store the current data frame into a temp variable
        df2 = self.construct_df()
        self.df = df1.append(df2, ignore_index=True)  # adding new row into the dataframe
        self.refresh_table()

    def delete_row(self):
        # delete the selected row
        index_list = []  # to store list of selected rows

        for model_index in self.tableView.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)  # append the selected indices into index_list

        for index in index_list:  # delete all selected rows
            tempDf = self.df
            self.df = tempDf.drop(index.row())  # delete each selected row from the dataframe

        self.df = self.df.reset_index(drop=True)  # reset the index in numerical order
        self.refresh_table()

    def save_csv(self):
        # save the dataframe into .csv file (ignoring the index)
        self.df.to_csv("./rw_supplier/rwSupplierList.csv", index=False)

    def search_query(self):
        # to filter out data that does not match with the search bar
        self.proxy.setFilterFixedString(self.searchBar.text())
