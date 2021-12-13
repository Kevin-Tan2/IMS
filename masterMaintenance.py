from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
from tableViewModel import tableModel, load_csv


class MasterMaintenance(QtWidgets.QMainWindow):

    def __init__(self, uiFilePath, csvFilePath, columnNames):
        super().__init__()

        self.uiFilePath = uiFilePath        # store the .ui file path
        self.csvFilePath = csvFilePath      # store the .csv file Path
        self.columnNames = columnNames      # the column/header names array used in data frame

        # load ui file
        loadUi(uiFilePath, self)

        # create data frame from csv file or column names
        self.df = load_csv(csvFilePath, self.columnNames)

        # create table model based of the object data frame
        self.model = tableModel(self.df)

        # create proxy model to enable search function
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)  # case insensitivity
        self.proxy.setFilterKeyColumn(-1)  # -1 search all columns

        # create table view model
        self.tableView.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.tableView.setModel(self.proxy)  # to set the proxy model into the table view

        # event responses
        self.resetButton.clicked.connect(self.reset_entries)
        self.addButton.clicked.connect(self.add_df)
        self.deleteButton.clicked.connect(self.delete_row)
        self.saveButton.clicked.connect(self.save_csv)
        self.searchBar.textChanged.connect(self.search_query)

    def reset_entries(self):
        pass

    def construct_df(self):
        pass

    def refresh_table(self):
        # reset the index in numerical order
        self.df = self.df.reset_index(drop=True)

        # refresh the table whenever data frame has been changed
        self.model = tableModel(self.df)
        self.proxy.setSourceModel(self.model)
        self.tableView.setModel(self.proxy)

    def add_df(self, df):
        # adding new data into the dataframe
        tempDf = self.df  # store the current data frame into a temp variable
        self.df = tempDf.append(df, ignore_index=True)  # adding new row into the dataframe
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

        self.refresh_table()

    def save_csv(self, csvFilePath):
        self.refresh_table()
        # save the dataframe into .csv file (ignoring the index)
        self.df.to_csv(csvFilePath, index=False)

    def search_query(self):
        # to filter out data that does not match with the search bar
        self.proxy.setFilterFixedString(self.searchBar.text())
