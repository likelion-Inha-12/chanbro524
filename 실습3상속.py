from 실습2클래스 import money

class saving(money):
    def newtech(self,interest,inmoney):
        print("계좌잔액은 {0}원 입니다".format(self.rest))
        print("이자율:{0}%".format(interest))
        print("{0}원 입금됐습니다".format(inmoney))
        interestmoney=(self.rest+inmoney)*(interest/100)
        print("{0}원의 이자가 추가됐습니다".format(interestmoney))
        self.rest=self.rest+interestmoney+inmoney
a=saving('이찬형',10000)
a.newtech(5,500)

