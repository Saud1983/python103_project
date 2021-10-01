
from random import randint

class BankAccount:

    def account_setter(self, national_id):
        self.account_id = national_id + randint(1000, 9999)
        self.balance = 0
        self.type = 'normal'
        self.passowrd = '0000'

    def account_display(self,):
        print(f"Account ID is : {self.account_id} ")
        print(f"Account Balance ID is : {self.balance}")
        print(f"Account Type is : {self.type}")

    def Deposit_setter(self, add):
        self.balance = self.balance + int(add)

    def withdraw_setter(self, deduct):
        self.balance = self.balance - int(deduct)

class Owner(BankAccount):

    def __init__(self, n_id, f_name, l_name, mobile):
        self.first_name = f_name
        self.last_name = l_name
        self.national_id = n_id
        self.mobile = mobile
        super(Owner, self).account_setter(self.national_id)

    def personal_display(self,):
        print(f"Client Name is : {self.first_name} {self.last_name} ")
        print(f"Client national ID is : {self.national_id}")
        print(f"Client national ID is : {self.mobile}")


client1 = Owner(1000000000, 'Saud', 'Alghamdi', 500053197)

client1.Deposit_setter(15000)
client1.withdraw_setter(8000)
client1.account_display()
client1.personal_display()
