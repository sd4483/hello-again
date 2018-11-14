class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self,amount):
        self.balance=self.balance-amount
    
    def deposit(self,amount):
        self.balance=self.balance+amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class CheckingAcc(Account):
    """This class generates checking accounts objects"""
    type = "checking"
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee
    
    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee

account=Account("balance.txt")
print(account.balance)
#account.withdraw(200)
#account.deposit(500)
account.commit()
print(account.balance)

sd_checking=CheckingAcc("sd.txt",1)
sd_checking.transfer(200)
sd_checking.commit()
print(sd_checking.balance)
print(sd_checking.type)

paturi_checking=CheckingAcc("paturi.txt",1)
paturi_checking.transfer(200)
paturi_checking.commit()
print(paturi_checking.balance)
print(paturi_checking.type)

print(sd_checking.__doc__)