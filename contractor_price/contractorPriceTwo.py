import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt
from masterMaintenance import MasterMaintenance
from tableViewModel import tableModel, load_csv
from contractor_price.contractorPriceOne import ContractorPriceOne
import pandas as pd


class ContractorPriceTwo(ContractorPriceOne):

    def __init__(self):
        uiFilePath = "./contractor_price/contractorPriceTonnage.ui"
        csvFilePathOne = "./contractor_price/TonnagePriceWetWood.csv"
        csvFilePathTwo = "./contractor_price/TonnagePriceDryWood.csv"
        columnNames = ['Size1', 'Size2', 'Price']
        super().__init__(uiFilePath, csvFilePathOne, csvFilePathTwo, columnNames)

    def reset_entries(self, tableNo=0):

        if tableNo == 0:
            self.wetHeight.clear()
            self.wetWidth.clear()
            self.wetPrice.clear()

        elif tableNo == 1:
            self.dryHeight.clear()
            self.dryWidth.clear()
            self.dryPrice.clear()

    def construct_df(self, index):
        # index 0 means wet wood, index 1 means dry wood
        height = [str(self.wetHeight.text()), str(self.dryHeight.text())]
        width = [str(self.wetWidth.text()), str(self.dryWidth.text())]
        price = [str(self.wetPrice.text()), str(self.dryPrice.text())]

        df = pd.DataFrame({'Size1': [height[index]], 'Size2': [width[index]], 'Price': [price[index]]})

        return df