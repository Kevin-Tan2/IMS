import sys

from PyQt5 import QtWidgets

from masterMaintenance import MasterMaintenance
import pandas as pd


class FWRWSpecies(MasterMaintenance):

    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "fwrwSpecies.ui"
        self.csvFilePath = currentDir + "fwrwSpeciesList.csv"

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

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    contractorEntry = FWRWSpecies()
    contractorEntry.show()
    sys.exit(app.exec_())
