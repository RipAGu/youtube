from AddPlaylistWindow import AddPlaylistWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from Database import Database
from Common import Common
import sys
class PlaylistPage(QtWidgets.QDialog):
    def __init__(self, mainUi, userName, nowId):
        super().__init__()
        self.playlistList = []
        self.playlistBtnList = []
        self.deleteBtnList = []
        self.playlistNoList = []
        self.mainUi = mainUi
        self.nowId = nowId
        userName = sum(userName, ())
        self.userName = ''.join(userName)
        self.playlistName = None
        self.mainUi.nameLabel.setText("유저 : " + self.userName)
        self.mainUi.addPlaylistBtn.clicked.connect(self.addPlaylistBtnEvent)
        self.mainUi.playlistBackBtn.clicked.connect(self.playlistBackBtnEvent)
        self.db = Database()
        self.updatePlaylist()
        
        

    def addPlaylistBtnEvent(self):
        self.addPage = AddPlaylistWindow()
        self.addPage.createBtn.clicked.connect(self.createBtnEvent)
        self.addPage.nameInput.returnPressed.connect(self.createBtnEvent)

    
    def createBtnEvent(self):
        information = Common(self.mainUi)
        self.playlistName = self.addPage.nameInput.text()
        if len(self.playlistName) == 0:
            information.InfoMessage("Warning", "최소 1자를 입력해주세요!", 2)
        else:
            nameList = []
            self.db.createData("playlist", ["id", "name"], [self.nowId, self.playlistName])
            self.addPage.Mainwindow.close()
            self.addPlaylist()

    def addPlaylist(self):
        lastNo = self.db.readData(["no"], "playlist", "name", [self.playlistName])
        lastNo = sum(lastNo, ())
        print(lastNo)
        self.playlistNoList.append(lastNo[-1])
        
        print(self.playlistNoList)
        
        self.playlistList.append(self.playlistName)
        tmpbtn = QtWidgets.QPushButton(self.mainUi.scrollAreaWidgetContents)
        tmpbtn.setStyleSheet(
            "background-color : white;"
        )
        tmpbtn.setMinimumSize(QtCore.QSize(380, 50))
        tmpdeleteBtn = QtWidgets.QPushButton(self.mainUi.scrollAreaWidgetContents)
        tmpdeleteBtn.setStyleSheet(
            "background-color : white;"
        )
        tmpdeleteBtn.setMinimumSize(QtCore.QSize(20, 50))
        self.mainUi.formLayout.setWidget(len(self.playlistList), QtWidgets.QFormLayout.LabelRole, tmpbtn)
        self.mainUi.formLayout.setWidget(len(self.playlistList), QtWidgets.QFormLayout.FieldRole, tmpdeleteBtn)
        tmpbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        tmpdeleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        tmpbtn.setText(self.playlistName)
        tmpdeleteBtn.setText("삭제")
        self.playlistBtnList.append(tmpbtn)
        self.deleteBtnList.append(tmpdeleteBtn)
        point = len(self.playlistList) - 1
        self.playlistBtnList[point].clicked.connect(lambda event, nowIndex = point : self.playlistBtnEvent(event, nowIndex))
        self.deleteBtnList[point].clicked.connect(lambda event, nowIndex = point :  self.deleteBtnEvent(event, point))
        

    def playlistBackBtnEvent(self):
        self.mainUi.stackedWidget.setCurrentIndex(0)
        for index in range(len(self.playlistList)):
            self.playlistBtnList[index].deleteLater()
            self.deleteBtnList[index].deleteLater()
        del self.playlistList
        del self.deleteBtnList
        del self.playlistBtnList
        del self.playlistNoList 
            

    def playlistBtnEvent(self, event, point):
        print(self.playlistNoList[point])
        self.mainUi.stackedWidget.setCurrentIndex(3)

        
        
        pass

    def deleteBtnEvent(self, event, point):
        information = Common(self.mainUi)
        reply = information.yesnoMessage("Warning", "삭제하시겠습니까?")
        if reply == True:
            print(point)
            self.playlistBtnList[point].deleteLater()
            self.deleteBtnList[point].deleteLater()
            self.db.deleteData("playlist", "no", [self.playlistNoList[point]])
            del self.playlistList[point]
            del self.playlistBtnList[point]
            del self.deleteBtnList[point]
            del self.playlistNoList[point]

            for index in range(point, len(self.playlistList)):
                self.playlistBtnList[index].disconnect()
                self.deleteBtnList[index].disconnect()
                self.playlistBtnList[index].clicked.connect(lambda event, nowIndex = index : self.playlistBtnEvent(event, nowIndex))
                self.deleteBtnList[index].clicked.connect(lambda event, nowIndex = index: self.deleteBtnEvent(event, nowIndex))
        else:
            pass
    def updatePlaylist(self):
        self.playlistNoList = self.db.readData(["no"], "playlist", "id", [self.nowId])
        self.playlistNoList = sum(self.playlistNoList, ())
        self.playlistNoList = list(self.playlistNoList)
        self.playlistList = self.db.readData(["name"], "playlist", "id", [self.nowId])
        self.playlistList = sum(self.playlistList, ())
        self.playlistList = list(self.playlistList)

        for index in range(0, len(self.playlistList)):
            tmpbtn = QtWidgets.QPushButton(self.mainUi.scrollAreaWidgetContents)
            tmpbtn.setStyleSheet(
                "background-color : white;"
            )
            tmpbtn.setMinimumSize(QtCore.QSize(380, 50))
            tmpdeleteBtn = QtWidgets.QPushButton(self.mainUi.scrollAreaWidgetContents)
            tmpdeleteBtn.setStyleSheet(
                "background-color : white;"
            )
            tmpdeleteBtn.setMinimumSize(QtCore.QSize(20, 50))
            self.mainUi.formLayout.setWidget(index, QtWidgets.QFormLayout.LabelRole, tmpbtn)
            self.mainUi.formLayout.setWidget(index, QtWidgets.QFormLayout.FieldRole, tmpdeleteBtn)
            tmpbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            tmpdeleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            tmpbtn.setText(self.playlistList[index])
            tmpdeleteBtn.setText("삭제")
            self.playlistBtnList.append(tmpbtn)
            self.deleteBtnList.append(tmpdeleteBtn)
            self.playlistBtnList[index].clicked.connect(lambda event, nowIndex = index : self.playlistBtnEvent(event, nowIndex))
            self.deleteBtnList[index].clicked.connect(lambda event, nowIndex = index : self.deleteBtnEvent(event, nowIndex))

        print(self.playlistList)
        pass
        
    
        


