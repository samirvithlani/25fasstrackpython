#public     self.name     everywhere
#protected  self._name    limited
#private    self.__name   not diectly accessible..


class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner #public
        self.__balance = balance #private...
        self._emi = 19000
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount #private access
    
    
    def get_Balacnce(self):
        return self.__balance


account = BankAccount("Ram",5000)
account.deposit(5000)    
print(account.get_Balacnce())

#print(f"account bakacne = {account.__balance}")
print(f"emi = {account._emi}")
        