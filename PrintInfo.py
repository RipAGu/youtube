from PyQt5 import QtWidgets
class PrintInfo:
    def __init__(self, mainUi):
        self.mainUi = mainUi

    def InfoMessage(self, kindMsg, msgcontent, movePage):
        msg = QtWidgets.QMessageBox()
        if kindMsg == "Critical":
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Warning")
        elif kindMsg == "Information":
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Information")
        elif kindMsg == "Warning":
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Warning")
        msg.setText(msgcontent)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            self.mainUi.stackedWidget.setCurrentIndex(movePage)


    def yesnoMessage(self, kindMsg, msgContent):
        reply = QtWidgets.QMessageBox()
        if kindMsg == "Critical":
            reply.setIcon(QtWidgets.QMessageBox.Critical)
            reply.setWindowTitle("Warning")
        elif kindMsg == "Information":
            reply.setIcon(QtWidgets.QMessageBox.Information)
            reply.setWindowTitle("Information")
        elif kindMsg == "Warning":
            reply.setIcon(QtWidgets.QMessageBox.Warning)
            reply.setWindowTitle("Warning")
        reply.setText(msgContent)
        reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        retval = reply.exec_()
        if retval == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False
