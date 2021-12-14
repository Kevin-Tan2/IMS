from masterMaintenance import MasterMaintenance
import pandas as pd


class RWChargeDuration(MasterMaintenance):

    def __init__(self):

        self.uiFilePath = "./rw_charge_duration/rwChargeDuration.ui"
        self.csvFilePath = "./rw_charge_duration/rwChargeDurationList.csv"
        self.columnNames = ['Range of Size', 'Expected Day']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)