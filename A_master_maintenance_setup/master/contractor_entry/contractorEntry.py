import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
from tableViewModel import tableModel, load_csv
from masterMaintenance import MasterMaintenance
import os.path
from pathlib import Path


class ContractorEntry(MasterMaintenance):
    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "contractorEntry.ui"
        self.csvFilePath = currentDir + "contractorList.csv"

        # create headers for .csv use
        self.columnNames = ['Division', 'Contractor ID', 'Contractor Name', 'Employee No', 'Contractor Type']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        # clear out the entries
        self.contractorID.clear()
        self.contractorName.clear()
        self.employeeNo.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        division = str(self.divBox.currentText())
        contractorID = str(self.contractorID.text())
        contractorName = str(self.contractorName.text())
        employeeNo = str(self.employeeNo.text())
        contractType = None
        if self.contractRadio.isChecked():
            contractType = str(self.contractRadio.text())

        elif self.nonContRadio.isChecked():
            contractType = str(self.nonContRadio.text())

        df = pd.DataFrame({'Division': [division],
                           'Contractor ID': [contractorID],
                           'Contractor Name': [contractorName],
                           'Employee No': [employeeNo],
                           'Contractor Type': [contractType]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = ContractorEntry()
    widget.show()
    sys.exit(app.exec_())
