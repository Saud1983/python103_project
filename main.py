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

    def deposit_setter(self, add):
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

running = True
used_sequence = []
current_client = []
# client1 = Owner(1000000000, 'Saud', 'Alghamdi', 500053197)
#
# client1.deposit_setter(15000)
# client1.withdraw_setter(8000)
# client1.account_display()
# client1.personal_display()

while running:
    choice = input("Enter the account number, '1' for creating new account, or '0' to stop the program :\n")
    # choices
    if choice == "1":
        for i in range(1, 100):
            if i not in used_sequence:
                add = True
                while add:
                    national_id = int(input("ID Please: \n"))
                    first_name = input('First name: \n')
                    last_name = input('Last name: \n')
                    mobile_no = int(input('mobile number: \n'))
                    print(f"Person's name is: '{first_name} {last_name}', ID {national_id}, Phone number is: '{mobile_no}'\n")
                    submit = input("Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()

                    if submit == "y":
                        globals()[f"client{i}"] = Owner(national_id, first_name, last_name, mobile_no)
                        used_sequence.append(i)
                        current_client.append(f"client{i}")
                        add = False
                break
        current_client[0].account_display()
        current_client[0].personal_display()
    elif choice == "0":
        running = False
    else:
        pass
