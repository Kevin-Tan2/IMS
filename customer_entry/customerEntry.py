import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
from tableViewModel import tableModel, load_csv
import os.path
from pathlib import Path


class CustomerEntry(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        uiFilePath = "./customer_entry/customerEntry.ui"
        csvFilePath = "./customer_entry/customerList.csv"

        # load the ui file
        loadUi(uiFilePath, self)

        # load the csv file as dataframe
        self._columnNames = ['Customer No', 'Customer ID', 'Customer Name', 'Addr1', 'Addr2', 'Addr3', 'Addr4',
                             'Tel No', 'GST Reg', 'Fax No', 'Account No']
        self._df = load_csv(csvFilePath, self._columnNames)
        self._df = self._df.sort_values('Customer ID')

        # table model
        self._model = tableModel(self._df)

        # filter proxy model for search functionality
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self._model)
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)  # case insensitivity
        self.proxy.setFilterKeyColumn(-1)  # -1 search all columns

        # table view model
        self.customerIDTable.horizontalHeader().setStretchLastSection(True)  # to stretch the header size to fit
        # self.customerIDTable.horizontalHeader().setStyleSheet("background-color: white;")
        self.customerIDTable.setSelectionBehavior(QAbstractItemView.SelectRows)  # to select entire row instead of cell
        self.customerIDTable.setModel(self.proxy)  # to set the proxy model into the table view

        for column_hidden in range(3, self._df.shape[1]):
            self.customerIDTable.hideColumn(column_hidden)  # hide other columns except Customer ID and Name

        # event responses
        self.resetButton.clicked.connect(self.reset_entries)
        self.saveButton.clicked.connect(self.save_csv)
        self.addButton.clicked.connect(self.add_df)
        self.deleteButton.clicked.connect(self.delete_row)
        self.closeButton.clicked.connect(self.close_window)
        self.searchBar.textChanged.connect(self.search_query)

    def close_window(self):
        self.switch_window.emit()

    def reset_entries(self):
        # clears the line entries
        self.inputCustomerID.clear()
        self.inputCustomerNo.clear()
        self.inputName.clear()
        self.inputAddrOne.clear()
        self.inputAddrTwo.clear()
        self.inputAddrThree.clear()
        self.inputAddrFour.clear()
        self.inputTelephone.clear()
        self.inputGST.clear()
        self.inputFax.clear()
        self.inputAccountNo.clear()

    def search_query(self):
        # to filter out data that does not match with the search bar
        self.proxy.setFilterFixedString(self.searchBar.text())

    def refresh_table(self):

        # sort by Customer ID ascending
        self._df = self._df.sort_values(by='Customer ID')

        # reset the index in numerical order
        self._df = self._df.reset_index(drop=True)

        # autofill the customer no
        for i in range(0, self._df.shape[0]):
            self._df.at[i, "Customer No"] = int(i + 1)

        # refresh the table whenever data frame has been changed
        self._model = tableModel(self._df)
        self.proxy.setSourceModel(self._model)
        self.customerIDTable.setModel(self.proxy)

        # self._df.shape[0] is the
        for column_hidden in range(3, self._df.shape[1]):
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
        df = pd.DataFrame({'Customer No': None,
                           'Customer ID': [customerID],
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
        self.refresh_table()
        # save the dataframe into .csv file (ignoring the index)
        self._df.to_csv("customer_entry/customerList.csv", index=False)

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

        self.refresh_table()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    customerEntry = CustomerEntry("./customerEntry.ui", "./customerList.csv")
    customerEntry.show()
    sys.exit(app.exec_())
