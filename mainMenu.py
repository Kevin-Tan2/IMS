import sys
import os
from PyQt5.QtCore import QPropertyAnimation
from login import login
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from A_master_maintenance_setup.masterMaintenanceSetup import MasterMaintenanceSetup


class MainMenu(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        loadUi("mainMenu.ui", self)

        self.buttonA.clicked.connect(lambda: self.switch_window.emit('A'))


class Controller:

    def __init__(self):
        self.loginPage = login.LoginPage("./login/login.ui", "./login/listUsers.csv")
        self.mainMenu = MainMenu()

        # setup MasterMaintenanceSetup class from A_master_maintenance_setup
        self.masterSetup = MasterMaintenanceSetup("A_master_maintenance_setup")

    def show_login(self):
        # display login page
        self.loginPage.show()

        # event response when the signal is emitted from the login page
        self.loginPage.switch_window.connect(self.show_main_menu)

    def show_main_menu(self):
        # close the login page
        self.loginPage.close()

        # display the customer entry
        self.mainMenu.show()

        # event response when the signal is emitted from the main menu
        self.mainMenu.switch_window.connect(self.show_section)

    def show_section(self, sectNo):

        self.mainMenu.hide()

        if sectNo == 'A':
            self.masterSetup.switch_window.connect(self.mainMenu.show)
            self.masterSetup.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
