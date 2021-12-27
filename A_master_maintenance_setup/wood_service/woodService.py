import sys
import icons_rc
from PyQt5.QtCore import QPropertyAnimation, QPoint, Qt
from PyQt5.QtWidgets import QVBoxLayout, QSizeGrip
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets

# Global value for the windows status
WINDOW_SIZE = 0


class WoodService(QtWidgets.QMainWindow):
    def __init__(self, currentDir=None):

        super().__init__()

        uiFilePath = "woodService.ui"

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + uiFilePath
        self.currentDir = currentDir

        # load the master.ui
        loadUi(self.uiFilePath, self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # to remove the default window frame
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # to give transparent background (provide round corners)
        self.oldPos = self.pos()

        # header's property
        self.closeBtn.clicked.connect(lambda: self.close())
        self.maxBtn.clicked.connect(lambda: self.toggle_max_restore())
        self.minBtn.clicked.connect(lambda: self.showMinimized())
        self.header.mouseMoveEvent = self.moveWindow

    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.oldPos = event.globalPos()

    def moveWindow(self, event):
        # if left mouse button is clicked (Only accept left mouse button clicks)
        if event.buttons() == Qt.LeftButton:
            # Move window
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    # Restore or maximize your window
    def toggle_max_restore(self):
        # Global windows state
        global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            self.showMaximized()

        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been set to normal size
            self.showNormal()


# Create main function to test the module individually
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = WoodService()
    widget.show()
    sys.exit(app.exec_())
