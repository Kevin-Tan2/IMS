import sys
from PyQt5 import QtWidgets, QtCore
import pandas as pd
from masterMaintenance import MasterMaintenance


class CustomerEntry(MasterMaintenance):

    def __init__(self):
        uiFilePath = "customerEntry.ui"
        csvFilePath = "customerList.csv"
        columnNames = ['Customer No', 'Customer ID', 'Customer Name', 'Addr1', 'Addr2', 'Addr3', 'Addr4',
                       'Tel No', 'GST Reg', 'Fax No', 'Account No']

        super().__init__(uiFilePath, csvFilePath, columnNames)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    customerEntry = CustomerEntry()
    customerEntry.show()
    sys.exit(app.exec_())