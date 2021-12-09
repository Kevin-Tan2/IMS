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
        loadUi("./contractor_entry/contractorEntry.ui", self)

        # create headers for .csv use
        self._columnNames = ['Division', 'Contractor ID', 'Contractor Name', 'Employee No', 'Contractor Type']

        # load contractorList.csv
        self._df = load_csv("./contractor_entry/contractorList.csv", self._columnNames)

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

        # event response
        self.resetButton.clicked.connect(self.reset_entries)
        self.addButton.clicked.connect(self.add_df)
        self.saveButton.clicked.connect(self.save_csv)
        self.deleteButton.clicked.connect(self.delete_row)
        self.searchBar.textChanged.connect(self.search_query)
        self.closeButton.clicked.connect(self.close)

    def reset_entries(self):

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

    def refresh_table(self):
        # refresh the table whenever data frame has been changed
        self._model = tableModel(self._df)
        self.proxy.setSourceModel(self._model)
        self.contractorTable.setModel(self.proxy)

    def add_df(self):
        # adding new data into the dataframe
        df1 = self._df  # store the current data frame into a temp variable
        df2 = self.construct_df()
        self._df = df1.append(df2, ignore_index=True)  # adding new row into the dataframe
        self.refresh_table()

    def save_csv(self):
        # save the dataframe into .csv file (ignoring the index)
        self._df.to_csv("./contractor_entry/contractorList.csv", index=False)

    def delete_row(self):
        # delete the selected row
        index_list = []  # to store list of selected rows

        for model_index in self.contractorTable.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)  # append the selected indices into index_list

        for index in index_list:  # delete all selected rows
            tempDf = self._df
            self._df = tempDf.drop(index.row())  # delete each selected row from the dataframe

        self._df = self._df.reset_index(drop=True)  # reset the index in numerical order
        self.refresh_table()

    def search_query(self):
        # to filter out data that does not match with the search bar
        self.proxy.setFilterFixedString(self.searchBar.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    contractorEntry = ContractorEntry()
    contractorEntry.show()
    sys.exit(app.exec_())
