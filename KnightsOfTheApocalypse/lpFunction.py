import numpy.random

class lpFunction:
    
    lpName = ""

    lpSynopsis = ""

    isGroup = 0

    lpAttack = 0

    lpTax = 0.12

    lpProbabilityOfAttack = 0.2

    def attackToOne(self, lpPeople):
        '''单体攻击'''
        # 被攻击者损失血量
        lpPeople.lpBloodVolume = lpPeople.lpBloodVolume - self.lpAttack
        # 如果被攻击者损失血量小于0
        if (lpPeople.lpBloodVolume <= 0):
            # 被攻击者死亡
            lpPeople.lpSurvive = 0

    def attackToAll(self, lpPeopleList):
        '''群体攻击：随机找几个人攻击'''
        numpy.random.shuffle(lpPeopleList)
        longth = len(lpPeopleList) * self.lpProbabilityOfAttack
        if longth < 0.5: longth = 0
        if (longth > 0.5) and (longth < 1): longth = 1
        longth = longth % 1
        for index in range(longth):
            people = lpPeopleList[index]
            # 被攻击者损失血量
            people.lpBloodVolume = people.lpBloodVolume - self.lpAttack
            # 如果被攻击者损失血量小于0
            if (people.lpBloodVolume <= 0):
                # 被攻击者死亡
                people.lpSurvive = 0

    def cutLeetToOne(self, lpPeople):
        '''单体割韭菜'''
        # 被割韭菜者损失金钱
        tureTax = lpPeople.lpMoney * self.lpTax
        lpPeople.lpMoney = lpPeople.lpMoney - tureTax
        return tureTax

    def cutLeetToAll(self, lpPeopleList):
        '''群体割韭菜'''
        tureTax = 0.0
        for lpPeople in lpPeopleList:
            # 被割韭菜者损失金钱
            tureTax = tureTax + lpPeople.lpMoney * self.lpTax
            lpPeople.lpMoney = lpPeople.lpMoney - lpPeople.lpMoney * self.lpTax
        return tureTax
