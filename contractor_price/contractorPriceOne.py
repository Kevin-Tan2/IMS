import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt
from masterMaintenance import MasterMaintenance
from tableViewModel import tableModel, load_csv
import pandas as pd


class ContractorPriceOne(MasterMaintenance):

    def __init__(self):
        self.uiFilePath = "./contractor_price/contractorPrice.ui"
        csvFilePathOne = "./contractor_price/contractorPriceWetWood.csv"
        csvFilePathTwo = "./contractor_price/contractorPriceDryWood.csv"

        self.csvFilePathArray = [csvFilePathOne, csvFilePathTwo]

        self.columnNames = ['Size1', 'Size2', 'Length', 'Price']

        super().__init__(self.uiFilePath, csvFilePathOne, self.columnNames)

        # create second dataframe for the second table
        self.df2 = load_csv(csvFilePathTwo, self.columnNames)

        self.dfArray = [self.df, self.df2]

        self.model2 = tableModel(self.df2)

        # create proxy model to enable search function
        self.proxy2 = QtCore.QSortFilterProxyModel(self)
        self.proxy2.setSourceModel(self.model2)
        self.proxy2.setFilterCaseSensitivity(Qt.CaseInsensitive)  # case insensitivity
        self.proxy2.setFilterKeyColumn(-1)  # -1 search all columns

        self.dryTableView.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.dryTableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.dryTableView.setModel(self.proxy2)  # to set the proxy model into the table view

        # event responses for table dry wood
        self.dryResetBtn.clicked.connect(lambda: self.reset_entries(1))
        self.dryAddBtn.clicked.connect(lambda: self.add_df(1))
        self.dryDeleteBtn.clicked.connect(self.delete_row)
        self.drySaveBtn.clicked.connect(lambda: self.save_csv(1))
        self.drySearchBar.textChanged.connect(self.search_dry_query)

    def reset_entries(self, tableNo=0):

        if tableNo == 0:
            self.wetHeight.clear()
            self.wetWidth.clear()
            self.wetLength.clear()
            self.wetPrice.clear()

        elif tableNo == 1:
            self.dryHeight.clear()
            self.dryWidth.clear()
            self.dryLength.clear()
            self.dryPrice.clear()

    def refresh_table(self, index=0):
        if index == 0:
            self.model = tableModel(self.dfArray[index])
            self.proxy.setSourceModel(self.model)
            self.tableView.setModel(self.proxy)

        elif index == 1:
            self.model2 = tableModel(self.dfArray[index])
            self.proxy2.setSourceModel(self.model2)
            self.dryTableView.setModel(self.proxy2)

    def construct_df(self, index):
        # index 0 means wet wood, index 1 means dry wood
        height = [str(self.wetHeight.text()), str(self.dryHeight.text())]
        width = [str(self.wetWidth.text()), str(self.dryWidth.text())]
        length = [str(self.wetLength.text()), str(self.dryLength.text())]
        price = [str(self.wetPrice.text()), str(self.dryPrice.text())]

        df = pd.DataFrame({'Size1': [height[index]], 'Size2': [width[index]],
                           'Length': [length[index]], 'Price': [price[index]]})

        return df

    def add_df(self, index=0):
        # adding new data into the dataframe
        tempDf = self.dfArray[index]  # store the current data frame into a temp variable
        self.dfArray[index] = tempDf.append(self.construct_df(index), ignore_index=True)  # append into the dataframe
        self.refresh_table(index)

    def save_csv(self, index=0):
        self.refresh_table(index)
        # save the dataframe into .csv file (ignoring the index)
        self.dfArray[index].to_csv(self.csvFilePathArray[index], index=False)

    def search_dry_query(self):
        # to filter out data that does not match with the search bar
        self.proxy2.setFilterFixedString(self.drySearchBar.text())