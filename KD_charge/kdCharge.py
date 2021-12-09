import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
from tableViewModel import tableModel, load_csv
import pandas as pd
import os.path
from pathlib import Path


class KDCharge(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        uiFilePath = "./kd_charge/kdCharge.ui"

        # load the ui file
        loadUi(uiFilePath, self)
