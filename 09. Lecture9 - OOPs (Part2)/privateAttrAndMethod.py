class Account:
    def __init__(self, accNo, accPass):
        self.accNo = accNo
        self.__accPass = accPass
    
    def resetPass(self):
        print(self.__accPass)

acc1 = Account(12345, "Hello@123")
print(acc1.accNo)
print(acc1.__accPass)
# print(acc1.resetPass())