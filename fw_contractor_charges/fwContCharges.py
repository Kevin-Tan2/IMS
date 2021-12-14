from masterMaintenance import MasterMaintenance


class FWContCharges(MasterMaintenance):

    def __init__(self):
        self.uiFilePath = "./fw_contractor_charges/fwContCharges.ui"
        self.csvFilePath = "./fw_contractor_charges/fwContChargesList.csv"
        self.columnNames = ['Length', 'Charges']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

        # sort by Customer ID ascending
        self.df = self.df.sort_values(by='Length')

