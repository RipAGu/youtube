from Common import Common
from Database import Database

class RegisterPage:
    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.mainUi.idDupBtn.clicked.connect(self.dupCheckBtnEvent)
        self.mainUi.registerApplyBtn.clicked.connect(self.registerBtnEvent)
        self.mainUi.registerBackBtn.clicked.connect(self.regiBackBtnEvent)
        self.dupCheck = False

    def dupCheckBtnEvent(self):
        db = Database()
        self.dupCheck = False
        idValue = self.mainUi.registerIdInput.text()
        nowIdList = []
        nowIdList = db.readData(["id"], "member", "id", [idValue])
        if len(idValue) == 0:
            self.mainUi.registerIdErrorLabel.setText("아이디를 입력해주세요!")
        elif len(idValue) < 8 or len(idValue) > 17:
            self.mainUi.registerIdErrorLabel.setText("아이디는 8~16자로 입력해주세요!")
        elif len(nowIdList) == 1:
            self.mainUi.registerIdErrorLabel.setText("중복된 아이디입니다.")
        else:
            self.mainUi.registerIdErrorLabel.setText("사용가능한 아이디입니다.")
            self.dupCheck = True
            self.mainUi.registerIdInput.setEnabled(False)

    def registerBtnEvent(self):
        db = Database()
        information = Common(self.mainUi)
        idValue = self.mainUi.registerIdInput.text()
        pwValueList = [] 
        for index in range(0, 2):
            pwValueList.append(self.mainUi.registerPwInputList[index].text())
        nameValue = self.mainUi.registerNameInput.text()

        if len(idValue) == 0:
            self.mainUi.registerIdErrorLabel.setText("아이디를 입력해주세요!")
        elif len(pwValueList[0]) == 0:
            self.mainUi.registerPwErrorLabel.setText("비밀번호를 입력해주세요!")
        elif len(pwValueList[1]) == 0:
            self.mainUi.registerPwErrorLabel.setText("비밀번호 확인을 해주세요!")
        elif len(nameValue) == 0:
            self.mainUi.registerNameErrorLabel.setText("이름을 입력해주세요!")
        
        elif self.dupCheck == False:
            self.mainUi.registerIdErrorLabel.setText("아이디 중복체크를 해주세요!")
        elif pwValueList[0] != pwValueList[1]:
            self.mainUi.registerPwErrorLabel.setText("비밀번호가 일치하지 않습니다!")
        else:
            memberInfoList = []
            pwValue = pwValueList[0]
            memberInfoList.append(idValue)
            memberInfoList.append(pwValue)
            memberInfoList.append(nameValue)
            db.createData("member", ["id", "pw", "name"], memberInfoList)
            information.InfoMessage("Information", "회원가입성공!", 0)
            self.mainUi.registerIdInput.clear()
            self.mainUi.registerNameInput.clear()
            for index in range(0, 2):
                self.mainUi.registerPwInputList[index].clear()
            self.dupCheck = False
            self.mainUi.registerIdErrorLabel.setText("")
            self.mainUi.registerPwErrorLabel.setText("")
            self.mainUi.registerNameErrorLabel.setText("")
            self.mainUi.registerIdInput.setEnabled(True)

    def regiBackBtnEvent(self):
        self.mainUi.registerIdInput.clear()
        self.mainUi.registerNameInput.clear()
        for index in range(0, 2):
            self.mainUi.registerPwInputList[index].clear()
        self.dupCheck = False
        self.mainUi.registerIdErrorLabel.setText("")
        self.mainUi.registerPwErrorLabel.setText("")
        self.mainUi.registerNameErrorLabel.setText("")
        self.mainUi.registerIdInput.setEnabled(True)
        self.mainUi.stackedWidget.setCurrentIndex(0)




            


            


