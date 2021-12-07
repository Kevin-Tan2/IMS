import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
import pandas as pd
import os.path
from pathlib import Path


class RWSupplier(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        uiPathFile = "./rw_supplier/rwSupplier.ui"

        # load ui file
        loadUi(uiPathFile, self)