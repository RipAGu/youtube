from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pyparsing import common_html_entity
from sympy import Q
from platform import system
from Common import Common
class MainUi:
    def __init__(self):
        self.common = Common([])
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setFixedSize(1600, 800)
        self.MainWindow.setWindowTitle("YouTube")
        self.centralWidget = QtWidgets.QWidget(self.MainWindow)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 810))
        self.stackedWidget.setStyleSheet(
            "background-color : black;"
        )
        
        self.loginPage = QtWidgets.QWidget()
        self.youtubeLogoLabel = QtWidgets.QLabel(self.loginPage)
        self.youtubeLogoLabel.setGeometry(QtCore.QRect(600, 50, 600, 250))
        pixmap = QtGui.QPixmap("./youtube-logo.jpg")
        self.youtubeLogoLabel.setPixmap(QtGui.QPixmap("./youtube-logo.jpg"))
        self.loginLabel = QtWidgets.QLabel(self.loginPage)
        self.font = self.common.setFont("Malgun Gothic", 20, True, 75)
        self.loginLabel.setGeometry(QtCore.QRect(650, 320, 100, 35))
        self.loginLabel.setFont(self.font)
        self.loginLabel.setStyleSheet(
            "color : white;"
        )
        self.loginLabel.setText("로그인")
        self.idPwLabelList = []
        self.font = self.common.setFont("Malgun Gothic", 15, [], [])
        for index in range(0, 2):
            idPwLabel = QtWidgets.QLabel(self.loginPage)
            idPwLabel.setGeometry(QtCore.QRect(590, 370 + index*50, 50, 30))
            idPwLabel.setStyleSheet(
                "color : white;"
            )
            idPwLabel.setFont(self.font)
            self.idPwLabelList.append(idPwLabel)
        self.idPwLabelList[0].setText("ID")
        self.idPwLabelList[1].setText("PW")
        self.idPwInputList = []
        for index in range(0, 2):
            idPwInput = QtWidgets.QLineEdit(self.loginPage)
            idPwInput.setGeometry(QtCore.QRect(650, 370 + 50*index, 300, 30))
            idPwInput.setStyleSheet(
                "background-color : white;"
            )
            self.idPwInputList.append(idPwInput)
        self.idPwInputList[1].setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginErrorLabel = QtWidgets.QLabel(self.loginPage)
        self.font = self.common.setFont("Malgun Gothic", 9, False, 75)
        self.loginErrorLabel.setGeometry(QtCore.QRect(650, 460, 300, 15))
        self.loginErrorLabel.setFont(self.font)
        self.loginErrorLabel.setStyleSheet(
            "color : red"
        )
        self.loginBtn = QtWidgets.QPushButton(self.loginPage)
        self.loginBtn.setGeometry(QtCore.QRect(650, 510, 300, 50))
        self.loginBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.font = self.common.setFont("Malgun Gothic", 12, False, [])
        self.loginBtn.setFont(self.font)
        self.loginBtn.setText("로그인")
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerPageBtn = QtWidgets.QPushButton(self.loginPage)
        self.registerPageBtn.setGeometry(QtCore.QRect(890, 565, 60, 30))
        self.registerPageBtn.setStyleSheet(
            "color : white;"
        )
        self.font = self.common.setFont("Malgun Gothic", 9, False, [])
        self.registerPageBtn.setFont(self.font)
        self.registerPageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerPageBtn.setText("회원가입")
        self.stackedWidget.addWidget(self.loginPage)





        self.registerPage = QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.registerPage)
        self.registerLogoLabel = QtWidgets.QLabel(self.registerPage)
        self.registerLogoLabel.setGeometry(QtCore.QRect(735, 80, 170, 45))
        self.font = self.common.setFont("Malgun Gothic", 25, True, 75)
        self.registerLogoLabel.setStyleSheet(
            "color : white;"
        )
        self.registerLogoLabel.setFont(self.font)
        self.registerLogoLabel.setText("회원가입")
        self.idLabel = QtWidgets.QLabel(self.registerPage)
        self.idLabel.setGeometry(QtCore.QRect(650, 180, 90, 20))
        self.idLabel.setStyleSheet(
            "color : white;"
        )
        self.font = self.common.setFont("Malgun Gothic", 12, False, [])
        self.idLabel.setFont(self.font)
        self.idLabel.setText("아이디")
        self.pwLabeList = []
        for index in range(0, 2):
            pwLabel = QtWidgets.QLabel(self.registerPage)
            pwLabel.setGeometry(QtCore.QRect(650, 280 + index*65, 140, 20))
            pwLabel.setStyleSheet(
                "color : white;"
            )
            pwLabel.setFont(self.font)
            self.pwLabeList.append(pwLabel)
        self.pwLabeList[0].setText("비밀번호")
        self.pwLabeList[1].setText("비밀번호 확인")
        self.registerIdLabel = QtWidgets.QLabel(self.registerPage)
        self.registerIdLabel.setGeometry(QtCore.QRect(650, 445, 40, 20))
        self.registerIdLabel.setFont(self.font)
        self.registerIdLabel.setStyleSheet(
            "color : white;"
        )
        self.registerIdLabel.setText("이름")
        self.registerIdInput = QtWidgets.QLineEdit(self.registerPage)
        self.registerIdInput.setGeometry(QtCore.QRect(650, 210, 300, 30))
        self.registerIdInput.setStyleSheet(
            "background-color : white;"
        )
        self.registerPwInputList = []
        for index in range(0, 2):
            registerPwInput = QtWidgets.QLineEdit(self.registerPage)
            registerPwInput.setGeometry(QtCore.QRect(650, 310 + 60*index, 300, 30))
            registerPwInput.setStyleSheet(
                "background-color : white;"
            )
            registerPwInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.registerPwInputList.append(registerPwInput)
        self.registerNameInput = QtWidgets.QLineEdit(self.registerPage)
        self.registerNameInput.setGeometry(QtCore.QRect(650, 470, 300, 30))
        self.registerNameInput.setStyleSheet(
            "background-color : white;"
        )
        self.registerIdErrorLabel = QtWidgets.QLabel(self.registerPage)
        self.registerIdErrorLabel.setGeometry(QtCore.QRect(650, 250, 250, 15))
        self.registerIdErrorLabel.setStyleSheet(
            "color : red;"
        )
        self.font = self.common.setFont("Malgun Gothic", 9, False, [])
        self.registerIdErrorLabel.setFont(self.font)
        self.registerPwErrorLabel = QtWidgets.QLabel(self.registerPage)
        self.registerPwErrorLabel.setGeometry(QtCore.QRect(650, 410, 210, 15))
        self.registerPwErrorLabel.setStyleSheet(
            "color : red;"
        )
        self.registerPwErrorLabel.setFont(self.font)
        self.registerNameErrorLabel = QtWidgets.QLabel(self.registerPage)
        self.registerNameErrorLabel.setGeometry(QtCore.QRect(650, 510, 210, 15))
        self.registerNameErrorLabel.setStyleSheet(
            "color : red;"
        )
        self.registerNameErrorLabel.setFont(self.font)
        self.idDupBtn = QtWidgets.QPushButton(self.registerPage)
        self.idDupBtn.setGeometry(QtCore.QRect(970, 210, 70, 30))
        self.idDupBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.idDupBtn.setFont(self.font)
        self.idDupBtn.setText("중복확인")
        self.idDupBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerApplyBtn = QtWidgets.QPushButton(self.registerPage)
        self.registerApplyBtn.setGeometry(QtCore.QRect(650, 570, 300, 50))
        self.registerApplyBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.font = self.common.setFont("Malgun Gothic", 12, False, [])
        self.registerApplyBtn.setFont(self.font)
        self.registerApplyBtn.setText("회원가입")
        self.registerApplyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBackBtn = QtWidgets.QPushButton(self.registerPage)
        self.registerBackBtn.setGeometry(QtCore.QRect(890, 625, 60, 30))
        self.registerBackBtn.setStyleSheet(
            "color : white;"
        )
        self.font = self.common.setFont("Malgun Gothic", 9, False, [])
        self.registerBackBtn.setFont(self.font)
        self.registerBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBackBtn.setText("뒤로가기")




        

        self.playlistPage = QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.playlistPage)
        self.nameLabel = QtWidgets.QLabel(self.playlistPage)
        self.nameLabel.setGeometry(QtCore.QRect(30, 30, 150, 30))
        self.font = self.common.setFont("Malgun Gothic", 15, True, 75)
        self.nameLabel.setFont(self.font)
        self.nameLabel.setStyleSheet(
            "color : white;"
        )
        self.addPlaylistBtn = QtWidgets.QPushButton(self.playlistPage)
        self.addPlaylistBtn.setGeometry(QtCore.QRect(1250, 40, 150, 35))
        self.addPlaylistBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.font = self.common.setFont("Malgun Gothic", 10, True, 75)
        self.addPlaylistBtn.setFont(self.font)
        self.addPlaylistBtn.setText("+재생목록 추가")
        self.addPlaylistBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playlistBackBtn = QtWidgets.QPushButton(self.playlistPage)
        self.playlistBackBtn.setGeometry(QtCore.QRect(1430, 40, 150, 35))
        self.playlistBackBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.playlistBackBtn.setFont(self.font)
        self.playlistBackBtn.setText("뒤로가기")
        self.playlistBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scrollArea = QtWidgets.QScrollArea(self.playlistPage)
        self.scrollArea.setGeometry(QtCore.QRect(550, 140, 500, 560))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(100, 100, 300, 300))
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)

        self.videoPage =QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.videoPage)
        self.addVideoBtn = QtWidgets.QPushButton(self.videoPage)
        self.addVideoBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.addVideoBtn.setGeometry(QtCore.QRect(1250, 40, 150, 35))
        self.font = self.common.setFont("Malgun Gothic", 10, True, 75)
        self.addVideoBtn.setFont(self.font)
        self.addVideoBtn.setText("+ 영상추가")
        self.addVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.videoPageBackBtn = QtWidgets.QPushButton(self.videoPage)
        self.videoPageBackBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.videoPageBackBtn.setGeometry(QtCore.QRect(1430, 40, 150, 35))
        self.videoPageBackBtn.setFont(self.font)
        self.videoPageBackBtn.setText("뒤로가기")
        self.videoPageBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        # self.videoTable = QtWidgets.QListWidget(self.videoPage)
        # self.videoTable.setGeometry(QtCore.QRect(1250, 120, 190, 550))
        # self.videoTable.setStyleSheet(
        #     "color : white"
        # )
        # self.testIcon = QtGui.QIcon('./가위.gif')
        # self.iconItem = QtWidgets.QListWidgetItem(self.testIcon, "테스트")
        # self.font = self.common.setFont("Malgun Gothic", 20, False, [])
        # self.iconItem.setFont(self.font)
        # self.videoTable.setFont(self.font)
        # self.videoTable.autoScrollMargin()
        # for i in range(0, 40):
        #     self.videoTable.insertItem(i, self.iconItem)



        formLayout = QtWidgets.QFormLayout()
        groupbox = QtWidgets.QGroupBox()
        


        self.videoDeleteBtn = QtWidgets.QPushButton(self.videoPage)
        self.videoDeleteBtn.setGeometry(QtCore.QRect(1480, 120, 100, 25))
        self.videoDeleteBtn.setStyleSheet(
            "background-color : red;"
            "color : white;"
        )
        self.font = self.common.setFont("Malgun Gothic", 10, False, [])
        self.videoDeleteBtn.setFont(self.font)
        self.videoDeleteBtn.setText("삭제")
        self.videoDeleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.videoNameLabel = QtWidgets.QLabel(self.videoPage)
        self.videoNameLabel.setGeometry(QtCore.QRect(110, 670, 440, 20))
        self.videoNameLabel.setStyleSheet(
            "color :white;"
        )
    
    
        
        
    
       

        




    

        
        # for index in range(0, 20):
        #     testBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #     # testBtn.setGeometry(QtCore.QRect(0, 0 + 50*index, 100, 30))
        #     testBtn.setStyleSheet(
        #         "background-color : white;"
        #     )
        #     # self.formLayout.addWidget(testBtn)
        #     testBtn.setMinimumSize(QtCore.QSize(380, 50))
        #     testbtn2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #     testbtn2.setStyleSheet(
        #         "background-color : white;"
        #     )
        #     testbtn2.setMinimumSize(QtCore.QSize(20, 50))
        #     # self.formLayout.addRow(testBtn, testBtn)
        #     self.formLayout.setWidget(index, QtWidgets.QFormLayout.LabelRole, testBtn)
        #     self.formLayout.setWidget(index, QtWidgets.QFormLayout.FieldRole, testbtn2)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)



            



        















        self.MainWindow.setCentralWidget(self.centralWidget)
        self.stackedWidget.setCurrentIndex(3)
        self.MainWindow.show()


    def setFont(self, fontName, fontSize, useBold, fontweight):
        self.font = QtGui.QFont()
        self.font.setFamily(fontName)
        self.font.setPointSize(fontSize)
        if useBold == True:
            self.font.setBold(useBold)
            self.font.setWeight(fontweight)
            


        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = MainUi()
    sys.exit(app.exec_())