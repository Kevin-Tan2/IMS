import pandas as pd
from pathlib import Path
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt


class tableModel(QAbstractTableModel):
    # table model is taken from https://learndataanalysis.org/display-pandas-dataframe-with-pyqt5-qtableview-widget/
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
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
