import pandas as pd

from masterMaintenance import MasterMaintenance


class FWContCharges(MasterMaintenance):

    def __init__(self):
        self.uiFilePath = "./fw_contractor_charges/fwContCharges.ui"
        self.csvFilePath = "./fw_contractor_charges/fwContChargesList.csv"
        self.columnNames = ['Length', 'Charges']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

        # sort by length ascending
        self.df = self.df.sort_values(by='Length')

    def reset_entries(self):
        self.length.clear()
        self.charges.clear()

    def refresh_table(self):
        # sort by Customer ID ascending
        self.df = self.df.sort_values(by='Length')

        super().refresh_table()

    def construct_df(self):
        length = str(self.length.text())
        charges = str(self.charges.text())

        df = pd.DataFrame({'Length': [length], 'Charges': [charges]})

        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self, csvFilePath):
        super().save_csv(self.csvFilePath)