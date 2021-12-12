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
