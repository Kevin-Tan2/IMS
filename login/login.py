import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class LoginPage(QtWidgets.QDialog):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, uiFilePath, csvFilePath):
        super().__init__()

        loadUi(uiFilePath, self)
        self.inputPass.setEchoMode(QtWidgets.QLineEdit.Password)  # hide the password
        self.loginButton.clicked.connect(self.check_password)
        self._csv = csvFilePath

    def check_password(self):
        # create a message box to inform the user if the login succeed or failed
        msg = QtWidgets.QMessageBox()

        try:
            # open the csv file consists of usernames and their password
            df = pd.read_csv(self._csv)

            # get the column position of Password
            passCol = df.columns.get_loc("Password")

            # get the column position of username
            userCol = df.columns.get_loc("Username")

            # get the row position of the specific username
            row = df.loc[df["Username"] == self.inputUser.text()].index[0]

            # check if there are any existing username and their matching password
            if self.inputUser.text() == str(df.iloc[row, userCol]) and self.inputPass.text() == str(
                    df.iloc[row, passCol]):
                msg.setText("Success")
                msg.exec_()
                self.switch_window.emit()
                #app.quit()

            else:
                msg.setText("Incorrect Username or Password")
                msg.exec_()

        except:
            msg.setText("This username does not exist")
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginPage = LoginPage("login.ui", "listUsers.csv")
    loginPage.show()
    sys.exit(app.exec_())
