import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
from tableViewModel import tableModel, load_csv
from masterMaintenance import MasterMaintenance
import pandas as pd
import os.path
from pathlib import Path


class KDCharge(MasterMaintenance):

    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "kdCharge.ui"
        self.csvFilePath = currentDir + "kdChargeList.csv"
        self.columnNames = ['Customer ID', 'Size', 'Price', 'Wood Type', 'Type', 'Species']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clears the line entries
        self.customerID.clear()
        self.length.clear()
        self.width.clear()
        self.price.clear()
        self.species.clear()

    def radio_select(self, selectType):
        text = None

        if selectType == 'Type':
            # radio button for type entry
            if self.tonnageBtn.isChecked():
                text = str(self.tonnageBtn.text())

            elif self.speciesBtn.isChecked():
                text = str(self.speciesBtn.text())

        elif selectType == 'Wood Type':
            # radio button for wood type entry
            if self.forestBtn.isChecked():
                text = str(self.forestBtn.text())

            elif self.rubberBtn.isChecked():
                text = str(self.rubberBtn.text())

        return text

    def construct_df(self):
        customerID = str(self.customerID.text())
        length = str(self.length.text())
        width = str(self.width.text())
        size = length + 'x' + width
        price = str(self.price.text())
        species = str(self.species.text())
        typeRadio = self.radio_select('Type')
        woodType = self.radio_select('Wood Type')

        df = pd.DataFrame({'Customer ID': [customerID],
                           'Size': [size],
                           'Price': [price],
                           'Wood Type': [woodType],
                           'Type': [typeRadio],
                           'Species': [species]})

        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = KDCharge()
    widget.show()
    sys.exit(app.exec_())
