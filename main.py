import sys
from login import login
from customer_entry import customerEntry
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi


class Controller:

    def __init__(self):
        self.customerEntry = customerEntry.CustomerEntry("./customer_entry/customerEntry.ui", "customer_entry"
                                                                                              "/customerList.csv")
        self.loginPage = login.LoginPage("./login/login.ui", "./login/listUsers.csv")

    def show_login(self):
        # display login page
        self.loginPage.show()

        # event response when the signal is emitted from the login page
        self.loginPage.switch_window.connect(self.show_main)

    def show_main(self):
        # close the login page
        self.loginPage.close()

        # display the customer entry
        self.customerEntry.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
