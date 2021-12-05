import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
import os.path
from pathlib import Path


class tableModel(QAbstractTableModel):
    # table model is taken from https://learndataanalysis.org/display-pandas-dataframe-with-pyqt5-qtableview-widget/
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


def load_csv(fileName, columnNames):
    # check if the .csv file exist
    filePath = Path("./" + fileName)

    if not filePath.exists():
        # if the file path does not exist then create new empty dataframe and save it
        df = pd.DataFrame(columns=columnNames)

    else:
        df = pd.read_csv(fileName)

    return df


class ContractorEntry(QtWidgets.QMainWindow):
    def __init__(self):
        super(ContractorEntry, self).__init__()

        # load UI
        loadUi("contractorEntry.ui", self)

        # create headers for .csv use
        self._columnNames = ['Division', 'Contractor ID', 'Contractor Name', 'Employee No', 'Contractor Type']

        # load contractorList.csv
        self._df = load_csv("contractorList.csv", self._columnNames)

        # create tableModel instance
        self._model = tableModel(self._df)

        # filter proxy model for search functionality
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self._model)
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)  # case insensitivity
        self.proxy.setFilterKeyColumn(-1)  # -1 search all columns

        # table view model
        self.contractorTable.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.contractorTable.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.contractorTable.setModel(self.proxy)  # to set the proxy model into the table view


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    contractorEntry = ContractorEntry()
    contractorEntry.show()
    sys.exit(app.exec_())
