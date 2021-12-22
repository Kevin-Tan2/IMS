import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
from tableViewModel import tableModel, load_csv
import pandas as pd
import os.path
from pathlib import Path


class UserMaintenance(QtWidgets.QMainWindow):

    def __init__(self, currentDir=None):
        super().__init__()

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "userMaintenanceEntry.ui"

        # load the ui file
        loadUi(self.uiFilePath, self)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = UserMaintenance()
    widget.show()
    sys.exit(app.exec_())
