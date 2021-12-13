import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAbstractItemView
from masterMaintenance import MasterMaintenance
from tableViewModel import tableModel, load_csv
import pandas as pd


class ContractorPriceOne(MasterMaintenance):

    def __init__(self):
        self.uiFilePath = "./contractor_price/contractorPrice.ui"
        self.csvFilePathOne = "./contractor_price/contractorPriceWetWood.csv"
        self.csvFilePathTwo = "./contractor_price/contractorPriceDryWood.csv"

        self.columnNames = ['Size1', 'Size2', 'Length', 'Price']

        super().__init__(self.uiFilePath, self.csvFilePathOne, self.columnNames)

        # create second dataframe for the second table
        self.df2 = load_csv(self.csvFilePathTwo, self.columnNames)

        self.model2 = tableModel(self.df2)

        self.tableView2.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.tableView2.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.tableView2.setModel(self.model2)  # to set the proxy model into the table view

        # event response for table wet wood
        self.resetButton.clicked.connect(lambda: self.reset_entries(0))

        # event responses for table dry wood
        self.dryResetBtn.clicked.connect(lambda: self.reset_entries(1))
        self.dryAddBtn.clicked.connect(self.add_df)
        self.dryDeleteBtn.clicked.connect(self.delete_row)
        self.drySaveBtn.clicked.connect(self.save_csv)
        self.drySearchBar.textChanged.connect(self.search_query)

    def reset_entries(self, tableNo):

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
