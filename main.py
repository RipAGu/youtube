from MainUi import MainUi
import os
import sys
from PyQt5 import QtWidgets
from LoginPage import LoginPage
class startProgram:
    def __init__(self):
        self.mainUi = MainUi()
        self.loginPage = LoginPage(self.mainUi)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    test = startProgram()
    sys.exit(app.exec_())
        

