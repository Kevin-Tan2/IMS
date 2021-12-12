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

        # create table view model
        self.tableView.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.tableView.setModel(self.model)  # to set the proxy model into the table view

        # event responses
        self.resetButton.clicked.connect(self.reset_entries)
        self.addButton.clicked.connect(self.add_df)

    def reset_entries(self):
        pass

    def construct_df(self):
        pass

    def refresh_table(self):
        # refresh the table whenever data frame has been changed
        self.model = tableModel(self.df)
        self.tableView.setModel(self.model)

    def add_df(self, df):
        # adding new data into the dataframe
        tempDf = self.df  # store the current data frame into a temp variable
        self.df = tempDf.append(df, ignore_index=True)  # adding new row into the dataframe
        self.refresh_table()
