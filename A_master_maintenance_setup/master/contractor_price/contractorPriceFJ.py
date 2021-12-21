import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt
from masterMaintenance import MasterMaintenance
from tableViewModel import tableModel, load_csv
import pandas as pd


class ContractorPriceFJ(MasterMaintenance):

    def __init__(self, uiFilePath="./contractor_price/contractorPriceFJ.ui",
                 csvFilePathOne="./contractor_price/FingerJointPrice.csv",
                 csvFilePathTwo="./contractor_price/FJbyMachinePrice.csv",
                 columnNames=None):

        if columnNames is None:
            columnNames = ['Size1', 'Size2', 'Price']

        self.uiFilePath = uiFilePath

        self.csvFilePathArray = [csvFilePathOne, csvFilePathTwo]

        self.columnNames = columnNames

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

        self.machineTableView.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.machineTableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.machineTableView.setModel(self.proxy2)  # to set the proxy model into the table view

        # event responses for table machine wood
        self.machineResetBtn.clicked.connect(lambda: self.reset_entries(1))
        self.machineAddBtn.clicked.connect(lambda: self.add_df(1))
        self.machineDeleteBtn.clicked.connect(lambda: self.delete_row(1))
        self.machineSaveBtn.clicked.connect(lambda: self.save_csv(1))
        self.machineSearchBar.textChanged.connect(self.search_machine_query)

    def reset_entries(self, tableNo=0):

        if tableNo == 0:
            self.height.clear()
            self.width.clear()
            self.price.clear()

        elif tableNo == 1:
            self.machineHeight.clear()
            self.machineWidth.clear()
            self.machinePrice.clear()

    def refresh_table(self, index=0):
        if index == 0:
            self.model = tableModel(self.dfArray[index])
            self.proxy.setSourceModel(self.model)
            self.tableView.setModel(self.proxy)

        elif index == 1:
            self.model2 = tableModel(self.dfArray[index])
            self.proxy2.setSourceModel(self.model2)
            self.machineTableView.setModel(self.proxy2)

    def construct_df(self, index):
        # index 0 means dry wood, index 1 means machine wood
        heightArray = [str(self.height.text()), str(self.machineHeight.text())]
        widthArray = [str(self.width.text()), str(self.machineWidth.text())]
        priceArray = [str(self.price.text()), str(self.machinePrice.text())]

        df = pd.DataFrame({'Size1': [heightArray[index]], 'Size2': [widthArray[index]], 'Price': [priceArray[index]]})

        return df

    def add_df(self, index=0):
        # adding new data into the dataframe
        tempDf = self.dfArray[index]  # store the current data frame into a temp variable
        self.dfArray[index] = tempDf.append(self.construct_df(index),
                                            ignore_index=True)  # append into the dataframe
        self.refresh_table(index)

    def save_csv(self, index=0):
        self.refresh_table(index)
        # save the dataframe into .csv file (ignoring the index)
        self.dfArray[index].to_csv(self.csvFilePathArray[index], index=False)

    def search_machine_query(self):
        # to filter out data that does not match with the search bar
        self.proxy2.setFilterFixedString(self.machineSearchBar.text())

    def delete_row(self, tableNo=0):
        # delete the selected row
        index_list = []  # to store list of selected rows

        if tableNo == 0:
            table = self.tableView

        elif tableNo == 1:
            table = self.machineTableView

        for model_index in table.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)  # append the selected indices into index_list

        for index in index_list:  # delete all selected rows
            tempDf = self.dfArray[tableNo]
            self.dfArray[tableNo] = tempDf.drop(index.row())  # delete each selected row from the dataframe

        self.refresh_table(tableNo)
