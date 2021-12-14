from masterMaintenance import MasterMaintenance
import pandas as pd


class FWRWSpecies(MasterMaintenance):

    def __init__(self):
        self.uiFilePath = "./fwrw_species/fwrwSpecies.ui"
        self.csvFilePath = "./fwrw_species/fwrwSpeciesList.csv"

        # create headers for .csv use
        self.columnNames = ['Species', 'Description']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

    def reset_entries(self):
        self.species.clear()
        self.description.clear()

    def construct_df(self):
        # construct a new data frame from the QLineEdits
        species = str(self.species.text())
        description = str(self.description.text())

        df = pd.DataFrame({'Species': [species], 'Description': [description]})

        return df

    def add_df(self):
        super().add_df(self.construct_df())
