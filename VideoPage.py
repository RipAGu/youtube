import platform
import os
import sys
import time
from pytest import Instance
import vlc
from urllib import request
from AddWindow import AddVideoWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from Database import Database
from Common import Common
import urllib.request
import pafy
class VideoPage:
    def __init__(self, mainUi, playlistNo):
        self.mainUi = mainUi
        self.playlistNo = playlistNo
        self.mainUi.addVideoBtn.clicked.connect(self.addVideoBtnEvent)
        self.mainUi.videoPageBackBtn.clicked.connect(self.videoPageBackBtn)
        for index in range(0, 5):
            self.mainUi.playerBtnList[index].clicked.connect(lambda event, nowIndex = index : self.playerBtnEvent(event, nowIndex))
        self.url = None
        self.groupBoxList = []
        self.urlList = []
        self.titleList = []
        self.thumbBtnList = []
        self.deleteBtnList = []
        self.videoNoList = []
        self.nowPlay = None
        self.db = Database()
        self.common = Common(self.mainUi)
        self.media = None
        self.mediaPlayer = None
        
        self.updateVideo()
    

    def playerBtnEvent(self, event, btnNo):
        if self.mediaPlayer != None:
            if btnNo == 0:
                self.mediaPlayer.previous()
            elif btnNo == 1:
                if self.mediaPlayer.is_playing() == False:
                    self.mediaPlayer.pause()
            elif btnNo == 2:
                if self.mediaPlayer.is_playing() == True:
                    self.mediaPlayer.pause()
            elif btnNo == 3:
                self.mediaPlayer.next()
            elif btnNo == 4:
                self.mediaPlayer.stop()

    def videoPageBackBtn(self):
        if self.mediaPlayer != None:
            self.mediaPlayer.stop()
        self.mainUi.addVideoBtn.clicked.disconnect()
        self.mainUi.videoPageBackBtn.clicked.disconnect()
        for index in range(0, len(self.videoNoList)):
            self.thumbBtnList[index].clicked.disconnect()
            self.deleteBtnList[index].clicked.disconnect()
            self.groupBoxList[index].deleteLater()
        
        self.mainUi.stackedWidget.setCurrentIndex(2)
     


    def addVideoBtnEvent(self):
        self.addPage = AddVideoWindow(self.mainUi)
        self.addPage.createBtn.clicked.connect(self.createBtnEvent)
        self.addPage.urlInput.returnPressed.connect(self.createBtnEvent)

    def createBtnEvent(self):
        information = Common(self.mainUi)
        
        self.url = self.addPage.urlInput.text()
        if len(self.url) == 0:
            information.InfoMessage("Warning", "최소 1자를 입력해주세요!", 3)
        else:
            self.addVideo()
            
    def addVideo(self):
        tmpUrl = self.addPage.urlInput.text()
        self.addPage.Mainwindow.close()
        self.video = pafy.new(tmpUrl)
        self.db.createData("video", ["name", "url", "playlist"], [self.video.title, tmpUrl, self.playlistNo])
        lastNo = self.db.readData(["no"], "video", "name", [self.video.title])
        lastNo = sum(lastNo, ())
        self.videoNoList.append(lastNo[-1])
        videothumbnail = self.video.thumb
        image = urllib.request.urlopen(videothumbnail).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image)
        icon = QtGui.QIcon()
        icon.addPixmap(pixmap)

        groupBox = QtWidgets.QGroupBox(self.mainUi.videoScrollWidgetContents)
        groupBox.setMinimumSize(QtCore.QSize(200, 200))
        self.font = self.common.setFont("Malgun Gothic", 10, False, [])
        groupBox.setFont(self.font)
        groupBox.setStyleSheet("color : white;")
        groupBox.setTitle(self.video.title)
        self.groupBoxList.append(groupBox)
        self.titleList.append(self.video.title)
        self.urlList.append(tmpUrl)
        
        thumbBtn = QtWidgets.QPushButton(groupBox)
        thumbBtn.setGeometry(QtCore.QRect(60, 40, 80, 80))
        thumbBtn.setStyleSheet("background-color : white;")
        thumbBtn.setIcon(icon)
        thumbBtn.setIconSize(QtCore.QSize(75, 75))
        deleteVideoBtn = QtWidgets.QPushButton(groupBox)
        deleteVideoBtn.setGeometry(QtCore.QRect(40, 140, 120, 25))
        deleteVideoBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        deleteVideoBtn.setText("삭제")
        thumbBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        deleteVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.thumbBtnList.append(thumbBtn)
        self.deleteBtnList.append(deleteVideoBtn)
        point = len(self.groupBoxList)-1
        self.mainUi.videoFormLayout.setWidget(point, QtWidgets.QFormLayout.FieldRole, groupBox)
        self.thumbBtnList[point].clicked.connect(lambda event, nowIndex = point : self.thumbBtnEvent(event, nowIndex))
        self.deleteBtnList[point].clicked.connect(lambda event, nowIndex = point : self.deleteBtnEvent(event, nowIndex))



    def thumbBtnEvent(self, event, point):
        self.nowPlay = point
        if self.mediaPlayer != None:
            if self.mediaPlayer.is_playing():
                self.mediaPlayer.stop()
        # video = pafy.new(self.urlList[point])
        # best = video.getbest()
        # playurl = best.url
        self.mediaPlayer = None
        playUrlList = []
        self.instance = vlc.Instance()
        self.mediaPlayer = self.instance.media_list_player_new()
        
        self.mediaList = self.instance.media_list_new()
        self.media = None
        
        for index in range(point, len(self.urlList)):
            video = pafy.new(self.urlList[index])


            best = video.getbest()
            playUrlList.append(best.url)
            media = self.instance.media_new(best.url)
            self.mediaList.add_media(media)
            self.mediaPlayer.set_media_list(self.mediaList)
        self.new = self.instance.media_player_new()
        self.mainUi.volumeBar.setValue(self.new.audio_get_volume())
        self.mainUi.volumeBar.valueChanged.connect(self.setVolume)
        self.new.set_hwnd(int(self.mainUi.videoFrame.winId()))
        self.mediaPlayer.set_media_player(self.new)

        self.mediaPlayer.play()

        # self.mediaPlayer.set_media(self.media)
        # self.mediaPlayer.set_hwnd(int(self.mainUi.videoFrame.winId()))
        # self.mediaPlayer.play()
        time.sleep(1)

    def setVolume(self, volume):
        self.new.audio_set_volume(volume)
    def deleteBtnEvent(self, event, point):
        information = Common(self.mainUi)
        reply = information.yesnoMessage("Warning", "삭제하겠습니까?")
        if reply == True:
            self.groupBoxList[point].deleteLater()
            self.db.deleteData("video", "no", [self.videoNoList[point]])
            del self.groupBoxList[point]
            del self.urlList[point] 
            del self.titleList[point]
            del self.thumbBtnList[point]
            del self.deleteBtnList[point]
            del self.videoNoList[point]

            for index in range(point, len(self.groupBoxList)):
                self.thumbBtnList[index].disconnect()
                self.deleteBtnList[index].disconnect()
                self.thumbBtnList[index].clicked.connect(lambda event, nowIndex = index : self.thumbBtnEvent(event, nowIndex))
                self.deleteBtnList[index].clicked.connect(lambda event, nowIndex = index : self.deleteBtnEvent(event, nowIndex))


        
    def updateVideo(self):
        dataList = self.db.readData(["no", "name", "url"], "video", "playlist", [self.playlistNo])
        for index in range(0, len(dataList)):
            self.videoNoList.append(dataList[index][0])
            self.titleList.append(dataList[index][1])
            self.urlList.append(dataList[index][2])
        

        for index in range(0, len(self.videoNoList)):
            video = pafy.new(self.urlList[index])
            videoThumbnail = video.thumb
            image = urllib.request.urlopen(videoThumbnail).read()
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image)
            icon = QtGui.QIcon()
            icon.addPixmap(pixmap)

            groupBox = QtWidgets.QGroupBox(self.mainUi.videoScrollWidgetContents)
            groupBox.setMinimumSize(QtCore.QSize(200, 200))
            self.font = self.common.setFont("Malgun Gothic", 10, False, [])
            groupBox.setFont(self.font)
            groupBox.setStyleSheet("color : white;")
            groupBox.setTitle(self.titleList[index])
            self.groupBoxList.append(groupBox)
            thumbBtn = QtWidgets.QPushButton(groupBox)
            thumbBtn.setGeometry(QtCore.QRect(60, 40, 80, 80))
            thumbBtn.setStyleSheet("background-color : white;")
            thumbBtn.setIcon(icon)
            thumbBtn.setIconSize(QtCore.QSize(75, 75))
            deleteVideoBtn = QtWidgets.QPushButton(groupBox)
            deleteVideoBtn.setGeometry(QtCore.QRect(40, 140, 120, 25))
            deleteVideoBtn.setStyleSheet(
                "background-color : red;"
                "color : white;"
            )
            deleteVideoBtn.setText("삭제")
            thumbBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            deleteVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            self.thumbBtnList.append(thumbBtn)
            self.deleteBtnList.append(deleteVideoBtn)
            self.mainUi.videoFormLayout.setWidget(index, QtWidgets.QFormLayout.FieldRole, groupBox)
            self.thumbBtnList[index].clicked.connect(lambda event, nowIndex = index : self.thumbBtnEvent(event, nowIndex))
            self.deleteBtnList[index].clicked.connect(lambda event, nowIndex = index : self.deleteBtnEvent(event, nowIndex))