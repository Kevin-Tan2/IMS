from masterMaintenance import MasterMaintenance
import pandas as pd


class RWChargeDuration(MasterMaintenance):

    def __init__(self):

        self.uiFilePath = "./rw_charge_duration/rwChargeDuration.ui"
        self.csvFilePath = "./rw_charge_duration/rwChargeDurationList.csv"
        self.columnNames = ['Range of Size', 'Expected Day']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

        # sort by Range of Size ascending
        self.df = self.df.sort_values(by='Range of Size')

    def reset_entries(self):

        self.size.clear()
        self.duration.clear()

    def refresh_table(self):
        # sort by Range of Size ascending
        self.df = self.df.sort_values(by='Range of Size')

        super().refresh_table()

    def construct_df(self):

        size = str(self.size.text())
        duration = str(self.duration.text())

        df = pd.DataFrame({'Range of Size': [size], 'Expected Day': [duration]})

        return df

    def add_df(self):
        super().add_df(self.construct_df())
