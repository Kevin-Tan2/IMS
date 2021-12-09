import sys

from PyQt5.QtCore import QAbstractTableModel, QPropertyAnimation
from login import login
from customer_entry import customerEntry
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import pandas as pd
import icons
from pathlib import Path


class tableModel(QAbstractTableModel):
    # table model is taken from https://learndataanalysis.org/display-pandas-dataframe-with-pyqt5-qtableview-widget/
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


def load_csv(fileName, columnNames):
    # check if the .csv file exist
    filePath = Path("./" + fileName)

    if not filePath.exists():
        # if the file path does not exist then create new empty dataframe and save it
        df = pd.DataFrame(columns=columnNames)

    else:
        df = pd.read_csv(fileName)

    return df


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        # load the main.ui

        loadUi("main.ui", self)
        self.animation = QPropertyAnimation(self.sideMenuContainer, b"maximumWidth")  # Animate minimumWidht

        # set event responses
        self.customerEntryBtn.clicked.connect(lambda: self.display(0))
        self.rwContBtn.clicked.connect(lambda: self.display(1))
        self.rwSupplierBtn.clicked.connect(lambda: self.display(2))
        self.sideMenuBtn.clicked.connect(self.toggleMenu)

    def display(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def toggleMenu(self):
        # Get current left menu width
        width = self.sideMenuContainer.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 228
        # If maximized
        else:
            # Restore menu
            newWidth = 0

        # Animate the transition
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


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
