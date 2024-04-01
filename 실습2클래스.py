class money:
    def __init__(self, name, rest):
        self.name = name
        self.rest = rest
    def inmoney(self,money):
        if money>0:
            print("{0}원 입금되었습니다".format(money))
            self.rest+=money
        else:
            False
    def outmoney(self,money):
        if money>0:
           if self.rest>=money:
                print("{0}원 출금되었습니다".format(money))
                self.rest-=money
           else:
               False 
        else:
            False
    def restmoney(self):
        print("{0}님의 잔액은{1}원입니다".format(self.name,self.rest))
a=money("이찬형",10000)
a.inmoney(500)
a.restmoney()