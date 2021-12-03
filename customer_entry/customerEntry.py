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


def load_csv(fileName):
    # check if the .csv file exist
    filePath = Path("./" + fileName)

    if not filePath.exists():
        # if the file path does not exist then create new empty dataframe and save it
        columnNames = ['Customer ID', 'Customer Name', 'Addr1', 'Addr2', 'Addr3', 'Addr4',
                       'Tel No', 'GST Reg', 'Fax No', 'Account No']
        df = pd.DataFrame(columns=columnNames)
        df.to_csv(fileName, index=False)

    else:
        df = pd.read_csv(fileName)

    return df


class CustomerEntry(QtWidgets.QMainWindow):
    def __init__(self):
        super(CustomerEntry, self).__init__()

        loadUi("customerEntry.ui", self)  # load the ui file
        self._df = load_csv("customerList.csv")

        # table model
        self._model = tableModel(self._df)

        # filter proxy model for search functionality
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self._model)
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)  # case insensitivity
        self.proxy.setFilterKeyColumn(-1)  # -1 search all columns

        # table view model
        self.customerIDTable.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        self.customerIDTable.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.customerIDTable.setModel(self.proxy)  # to set the proxy model into the table view
        for column_hidden in range(2, self._df.shape[1]):
            self.customerIDTable.hideColumn(column_hidden)  # hide other columns except Customer ID and Name

        # event responses
        self.saveButton.clicked.connect(self.save_csv)
        self.addButton.clicked.connect(self.add_df)
        self.deleteButton.clicked.connect(self.delete_row)
        self.closeButton.clicked.connect(self.close)
        self.searchBar.textChanged.connect(self.search_query)

    def search_query(self):
        # to filter out data that does not match with the search bar
        self.proxy.setFilterFixedString(self.searchBar.text())

    def refresh_table(self):
        # refresh the table whenever data frame has been changed
        self._model = tableModel(self._df)
        self.proxy.setSourceModel(self._model)
        self.customerIDTable.setModel(self.proxy)

        for column_hidden in range(2, self._df.shape[1]):
            self.customerIDTable.hideColumn(column_hidden)

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        customerID = str(self.inputCustomerID.text())
        customerName = str(self.inputName.text())
        customerType = str(self.customerTypeDropBox.currentText())
        addr1 = str(self.inputAddrOne.text())
        addr2 = str(self.inputAddrTwo.text())
        addr3 = str(self.inputAddrThree.text())
        addr4 = str(self.inputAddrFour.text())
        telNo = str(self.inputTelephone.text())
        gstReg = str(self.inputGST.text())
        faxNo = str(self.inputFax.text())
        accountNo = str(self.inputAccountNo.text())
        df = pd.DataFrame({'Customer ID': [customerID],
                           'Customer Name': [customerName],
                           'Customer Type': [customerType],
                           'Addr1': [addr1],
                           'Addr2': [addr2],
                           'Addr3': [addr3],
                           'Addr4': [addr4],
                           'Tel No': [telNo],
                           'GST Reg': [gstReg],
                           'Fax No': [faxNo],
                           'Account No': [accountNo]})
        return df

    def save_csv(self):
        # save the dataframe into .csv file (ignoring the index)
        self._df.to_csv("customerList.csv", index=False)

    def add_df(self):
        # adding new data into the dataframe
        df1 = self._df  # store the current data frame into a temp variable
        df2 = self.construct_df()
        self._df = df1.append(df2, ignore_index=True)  # adding new row into the dataframe
        self.refresh_table()

    def delete_row(self):
        # delete the selected row
        index_list = []  # to store list of selected rows

        for model_index in self.customerIDTable.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)  # append the selected indices into index_list

        for index in index_list:  # delete all selected rows
            tempDf = self._df
            self._df = tempDf.drop(index.row())  # delete each selected row from the dataframe

        self._df = self._df.reset_index(drop=True)  # reset the index in numerical order
        self.refresh_table()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    customerEntry = CustomerEntry()
    customerEntry.show()
    sys.exit(app.exec_())
