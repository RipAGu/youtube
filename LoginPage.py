from Database import Database
from MainUi import MainUi
from RegisterPage import RegisterPage
from PlaylistPage import PlaylistPage
class LoginPage:
    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.mainUi.loginBtn.clicked.connect(self.loginBtnEvent)
        self.mainUi.registerPageBtn.clicked.connect(self.registerPageBtnEvent)
        self.mainUi.idPwInputList[1].returnPressed.connect(self.loginBtnEvent)



    def loginBtnEvent(self):
        db = Database()
        idValue = self.mainUi.idPwInputList[0].text()
        pwValue = self.mainUi.idPwInputList[1].text()
        nowPwList = []
        nowPwList = db.readData(["pw"], "member", "id", [idValue])
        nowPwList = sum(nowPwList, ())
        if len(idValue) == 0:
            self.mainUi.loginErrorLabel.setText("아이디를 입력해주세요!")
        elif len(pwValue) == 0:
            self.mainUi.loginErrorLabel.setText("비밀번호를 입력해주세요!")
        elif pwValue in nowPwList: #로그인 성공
            self.mainUi.idPwInputList[0].clear()
            self.mainUi.idPwInputList[1].clear()
            nowName = db.readData(["name"], "member", "id", [idValue])    
                  
            self.playListPage = PlaylistPage(self.mainUi, nowName, idValue)
            self.mainUi.stackedWidget.setCurrentIndex(2)
            

        else:
            self.mainUi.loginErrorLabel.setText("아이디 또는 비밀번호를 확인해주세요!")

    def registerPageBtnEvent(self):
        self.regiPage = RegisterPage(self.mainUi)
        self.mainUi.stackedWidget.setCurrentIndex(1)
        

    





    

        

    