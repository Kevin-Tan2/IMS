import sys

from masterMaintenance import InvoiceWidget
import pandas as pd


class StorageInvoice(InvoiceWidget):

    def __init__(self):

        uiFilePath = "./storage_invoice/storageInvoiceNo.ui"
        csvFilePath = "./storage_invoice/storageInvoiceList.csv"
        columnNames = ['Invoice No']

        super().__init__(uiFilePath, csvFilePath, columnNames)

    def construct_df(self):
        df = pd.DataFrame({'Invoice No': [str(self.inputNo.text())]})
        return df

