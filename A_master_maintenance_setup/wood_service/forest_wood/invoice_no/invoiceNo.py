import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
from tableViewModel import tableModel, load_csv
from masterMaintenance import InvoiceWidget
import os.path
from pathlib import Path


class InvoiceNo(InvoiceWidget):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "invoiceNo.ui"
        self.csvFilePath = currentDir + "invoiceNo.csv"

        # create headers for .csv use
        self.columnNames = ['SerialNo']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = InvoiceNo()
    widget.show()
    sys.exit(app.exec_())