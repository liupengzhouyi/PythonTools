

class lpPeople:

    lpSurvive = 1

    lpName = ""

    lpAge = 0

    lpSecond = 60*365*24*60*60

    lpImageUrl = ""

    lpMoney = 0

    lpBloodValue = 100

    def lossMoney(self, money):
        self.lpMoney = self.lpMoney - money

    def lossBlood(self, blood):
        if (self.lpBloodValue > blood):
            self.lpBloodValue = self.lpBloodVaalue - blood
        else:
            self.lpBloodValue = 0
            self.lpSurvive = 0

    def addMoney(self, money):
        self.lpMoney = self.lpMoney + money

    def addBloodValue(self, blood):
        self.lpBloodValue = self.lpBloodValue + blood