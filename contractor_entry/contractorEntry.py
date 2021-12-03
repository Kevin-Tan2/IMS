import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
import os.path
from pathlib import Path


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
        super().__init__()

        # load UI
        loadUi("contractorEntry.ui", self)

        # create headers for .csv use
        columnNames = ['Division', 'Contractor ID', 'Contractor Name', 'Employee No', 'Contractor Type']

        # load contractorList.csv
        self._df = load_csv("contractorList.csv", columnNames)
