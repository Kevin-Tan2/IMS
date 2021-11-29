# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(351, 263)
        Login.setStyleSheet("background:rgb(103, 103, 103)")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")

        # create a login button
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(150, 180, 93, 28))
        self.loginButton.clicked.connect(self.check_password)

        # adjustments to colours
        self.loginButton.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.loginButton.setObjectName("loginButton")
        self.inputFrame = QtWidgets.QFrame(self.centralwidget)
        self.inputFrame.setGeometry(QtCore.QRect(60, 70, 231, 101))

        # frame to contain username and password objects
        self.inputFrame.setStyleSheet("color: rgb(255, 255, 255)")
        self.inputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputFrame.setObjectName("inputFrame")

        # create a line edit for username
        self.inputUsername = QtWidgets.QLineEdit(self.inputFrame)
        self.inputUsername.setGeometry(QtCore.QRect(90, 20, 111, 22))
        self.inputUsername.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);")
        self.inputUsername.setObjectName("inputUsername")

        # create a line edit for password
        self.inputPassword = QtWidgets.QLineEdit(self.inputFrame)
        self.inputPassword.setGeometry(QtCore.QRect(90, 60, 111, 22))
        self.inputPassword.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);")
        self.inputPassword.setObjectName("inputPassword")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)    # hide the password

        # username label
        self.usernameLabel = QtWidgets.QLabel(self.inputFrame)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.usernameLabel.setObjectName("usernameLabel")

        # password label
        self.passwordLabel = QtWidgets.QLabel(self.inputFrame)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.passwordLabel.setObjectName("passwordLabel")

        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login Page"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.usernameLabel.setText(_translate("Login", "Username"))
        self.passwordLabel.setText(_translate("Login", "Password"))

    # checking if the the username and the password are matched
    def check_password(self):

        # create a message box to inform the user if the login succeed or failed
        msg = QtWidgets.QMessageBox()

        if self.inputUsername.text() == 'admin' and self.inputPassword.text() == 'password':
            msg.setText('Success')
            msg.exec_()
            app.quit()

        else:
            msg.setText('Incorrect Password')
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
