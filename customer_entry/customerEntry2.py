import sys
from PyQt5 import QtWidgets, QtCore
import pandas as pd
from masterMaintenance import MasterMaintenance


class CustomerEntry(MasterMaintenance):

    def __init__(self):
        self.uiFilePath = "customerEntry.ui"
        self.csvFilePath = "customerList.csv"
        self.columnNames = ['Customer No', 'Customer ID', 'Customer Name', 'Addr1', 'Addr2', 'Addr3', 'Addr4',
                            'Tel No', 'GST Reg', 'Fax No', 'Account No']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

        # sort by Customer ID ascending
        self.df = self.df.sort_values(by='Customer ID')

        # hide columns from column 3 to maximum number of column
        for column_hidden in range(3, self.df.shape[1]):
            self.tableView.hideColumn(column_hidden)

    def refresh_table(self):
        # sort by Customer ID ascending
        self.df = self.df.sort_values(by='Customer ID')

        # reset the index in numerical order
        self.df = self.df.reset_index(drop=True)

        # autofill the customer no
        for i in range(0, self.df.shape[0]):
            self.df.at[i, "Customer No"] = int(i + 1)

        super().refresh_table()

        # self.df.shape[0] is the
        for column_hidden in range(3, self.df.shape[1]):
            self.tableView.hideColumn(column_hidden)

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
        df = pd.DataFrame({'Customer No': None, 'Customer ID': [customerID], 'Customer Name': [customerName],
                           'Customer Type': [customerType], 'Addr1': [addr1], 'Addr2': [addr2], 'Addr3': [addr3],
                           'Addr4': [addr4], 'Tel No': [telNo], 'GST Reg': [gstReg], 'Fax No': [faxNo],
                           'Account No': [accountNo]})
        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    customerEntry = CustomerEntry()
    customerEntry.show()
    sys.exit(app.exec_())