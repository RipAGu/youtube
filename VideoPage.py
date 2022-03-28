
from itertools import groupby
import time
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
        self.threadList = []
        
        self.updateVideo()
    

    def playerBtnEvent(self, event, btnNo):
        if self.mediaPlayer != None:
            if btnNo == 0:
                self.mediaPlayer.previous()
            elif btnNo == 1:
                if self.mediaPlayer.is_playing() == False:
                    self.mediaPlayer.play()
            elif btnNo == 2:
                if self.mediaPlayer.is_playing() == True:
                    self.mediaPlayer.pause()
            elif btnNo == 3:
                self.mediaPlayer.next()
            elif btnNo == 4:
                self.mediaPlayer.stop()

    def videoPageBackBtn(self):
        for index in range(0, len(self.threadList)):
            self.threadList[index].quit()
        if self.mediaPlayer != None:
            self.mediaPlayer.stop()
        self.mainUi.addVideoBtn.clicked.disconnect()
        self.mainUi.videoPageBackBtn.clicked.disconnect()
        for index in range(0, len(self.videoNoList)):
            self.thumbBtnList[index].clicked.disconnect()
            self.deleteBtnList[index].clicked.disconnect()
            self.groupBoxList[index].deleteLater()
        
        for index in range(0, 5):
            self.mainUi.playerBtnList[index].clicked.disconnect()
        try:
            self.mainUi.volumeBar.disconnect()
        except:
            pass
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
        try:
            self.db.createData("video", ["url", "playlist"], [tmpUrl, self.playlistNo])
            lastNo = self.db.readData(["no"], "video", "url", [tmpUrl])
            lastNo = sum(lastNo, ())
            self.videoNoList.append(lastNo[-1])

            groupBox = QtWidgets.QGroupBox(self.mainUi.videoScrollWidgetContents)
            groupBox.setMinimumSize(QtCore.QSize(200, 200))
            self.font = self.common.setFont("Malgun Gothic", 10, False, [])
            groupBox.setFont(self.font)
            groupBox.setStyleSheet("color : white;")
            self.groupBoxList.append(groupBox)
            self.urlList.append(tmpUrl)
            
            thumbBtn = QtWidgets.QPushButton(groupBox)
            thumbBtn.setGeometry(QtCore.QRect(60, 40, 80, 80))
            thumbBtn.setStyleSheet("background-color : white;")
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
            self.mainUi.videoFormLayout.setWidget(point+1, QtWidgets.QFormLayout.FieldRole, self.groupBoxList[point])
            self.thumbBtnList[point].clicked.connect(lambda event, nowIndex = point : self.thumbBtnEvent(event, nowIndex))
            self.deleteBtnList[point].clicked.connect(lambda event, nowIndex = point : self.deleteBtnEvent(event, nowIndex))

            videothread = VideoThread(tmpUrl, point, self.thumbBtnList[point], self.groupBoxList[point])
            self.threadList.append(videothread)
            self.threadList[-1].start()
        except:
            information = Common(self.mainUi)
            information.InfoMessage("Warning", "올바른 주소를 입력해주세요!", 3)

    def thumbBtnEvent(self, event, point):
        self.nowPlay = point
        if self.mediaPlayer != None:
            print()
            if self.mediaPlayer.is_playing() == True:
                self.mediaPlayer.stop()
            elif self.mediaPlayer.is_playing() == False:
                print(self.mediaPlayer.get_state())
                if self.mediaPlayer.get_state() == 6:
                    self.new.release()
                    self.mediaPlayer.release()
                    print("접근")
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

        # time.sleep(1) 멤버변수가 있어서 필요X 

    def setVolume(self, volume):
        self.new.audio_set_volume(volume)
    def deleteBtnEvent(self, event, point):
        information = Common(self.mainUi)
        reply = information.yesnoMessage("Warning", "삭제하겠습니까?")
        if reply == True:
            print(point)
            self.mainUi.videoFormLayout.removeRow(self.groupBoxList[point])
            print(self.videoNoList)
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
        dataList = self.db.readData(["no", "url"], "video", "playlist", [self.playlistNo])
        self.threadList = []
        for index in range(0, len(dataList)):
            self.videoNoList.append(dataList[index][0])
           
            self.urlList.append(dataList[index][1])
        print(self.urlList)
        

        for index in range(0, len(self.videoNoList)):
            videoThread = None
            groupBox = QtWidgets.QGroupBox(self.mainUi.videoScrollWidgetContents)
            groupBox.setMinimumSize(QtCore.QSize(200, 200))
            self.font = self.common.setFont("Malgun Gothic", 10, False, [])
            groupBox.setFont(self.font)
            groupBox.setStyleSheet("color : white;")
            self.groupBoxList.append(groupBox)
            thumbBtn = QtWidgets.QPushButton(groupBox)
            thumbBtn.setGeometry(QtCore.QRect(60, 40, 80, 80))
            thumbBtn.setStyleSheet("background-color : white;")
       
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

        for index in range(0, len(self.videoNoList)):
            videoThread = VideoThread(self.urlList[index], index, self.thumbBtnList[index], self.groupBoxList[index])
            self.threadList.append(videoThread)
            self.threadList[index].start()

           



   
class VideoThread(QtCore.QThread, QtCore.QObject):
    change = QtCore.pyqtSignal()
    def __init__(self, url, point, btn, groupBox):
        super().__init__()
        self.url = url
        self.point = point
        self.btn = btn
        self.groupBox = groupBox
        self.change.connect(self.loadImage)
        self.image = None

    def run(self):
        video = pafy.new(self.url)
        self.videoThumbnail = video.thumb
        self.videoTitle = video.title
        self.change.emit()

    def loadImage(self):
        self.groupBox.setTitle(self.videoTitle)
        self.image = urllib.request.urlopen(self.videoThumbnail).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.image)
        icon = QtGui.QIcon()
        icon.addPixmap(pixmap)
        self.btn.setIcon(icon)
        self.btn.setIconSize(QtCore.QSize(75, 75))

    



