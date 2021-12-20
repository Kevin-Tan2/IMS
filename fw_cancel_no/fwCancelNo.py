from masterMaintenance import InvoiceWidget
import pandas as pd


class FWCancel(InvoiceWidget):

    def __init__(self):

        uiFilePath = "./fw_cancel_no/fwCancelNo.ui"
        csvFilePath = "./fw_cancel_no/fwCancelList.csv"
        columnNames = ['Cancel No']

        super().__init__(uiFilePath, csvFilePath, columnNames)

    def construct_df(self):
        df = pd.DataFrame({'Cancel No': [str(self.inputNo.text())]})
        return df

    def refresh_input_text(self):
        if not self.df.empty:
            self.inputNo.setText(str(self.df['Cancel No'].iloc[-1]))