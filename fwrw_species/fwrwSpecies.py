from masterMaintenance import MasterMaintenance
import pandas as pd


class FWRWSpecies(MasterMaintenance):

    def __init__(self):
        self.uiFilePath = "./fwrw_species/fwrwSpecies.ui"
        self.csvFilePath = "./fwrw_species/fwrwSpeciesList.csv"

        # create headers for .csv use
        self.columnNames = ['Species', 'Description']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)
