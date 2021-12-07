import sys
from login import login
from customer_entry import customerEntry
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        # load the main.ui
        loadUi("main.ui", self)

        # set event responses
        self.customerEntryBtn.clicked.connect(self.customer_entry)

    def customer_entry(self):
        self.customerEntry = customerEntry.CustomerEntry("./customer_entry/customerEntry.ui",
                                                         "./customer_entry/customerList.csv")
        self.customerEntry.show()


class Controller:

    def __init__(self):
        self.mainWindow = MainWindow()
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
        self.mainWindow.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
