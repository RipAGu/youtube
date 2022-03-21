from PyQt5 import QtCore, QtWidgets, QtGui
import sys

class AddPlaylistWindow:
    def __init__(self):
        self.Mainwindow = QtWidgets.QMainWindow()
        self.Mainwindow.setFixedSize(300, 180)
        self.Mainwindow.setWindowTitle("Add Playlist")
        self.centralWidget = QtWidgets.QWidget(self.Mainwindow)
        self.Mainwindow.setStyleSheet(
            "background-color : black;"
        )
        self.Mainwindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.nameLabel = QtWidgets.QLabel(self.centralWidget)
        self.nameLabel.setGeometry(QtCore.QRect(40, 25, 60, 30))
        self.nameLabel.setStyleSheet(
            "color : white;"
        )
        self.setFont("Malgun Gothic", 12, False, [])
        self.nameLabel.setText("이름")
        self.nameLabel.setFont(self.font)
        self.nameInput = QtWidgets.QLineEdit(self.centralWidget)
        self.nameInput.setGeometry(QtCore.QRect(40, 75, 220, 30))
        self.nameInput.setStyleSheet(
            "background-color : white;"
        )
        self.createBtn = QtWidgets.QPushButton(self.centralWidget)
        self.createBtn.setGeometry(QtCore.QRect(100, 130, 100, 25))
        self.createBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.setFont("Malgun Gothic", 9, False, [])
        self.createBtn.setFont(self.font)
        self.createBtn.setText("만들기")
        self.createBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))





        self.Mainwindow.setCentralWidget(self.centralWidget)
        self.Mainwindow.show()

    def setFont(self, fontName, fontSize, useBold, fontweight):
        self.font = QtGui.QFont()
        self.font.setFamily(fontName)
        self.font.setPointSize(fontSize)
        if useBold == True:
            self.font.setBold(useBold)
            self.font.setWeight(fontweight)

    
