from random import randint
from pprint import pprint


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
        item['account_info']['account_balance'] = self.balance

    def withdraw_setter(self, deduct):
        self.balance = self.balance - int(deduct)
        item['account_info']['account_balance'] = self.balance



class Client(BankAccount):

    def __init__(self, client_id, n_id, f_name, l_name, mobile):
        self.client_id = client_id
        self.first_name = f_name
        self.last_name = l_name
        self.national_id1 = n_id
        self.mobile = mobile
        super(Client, self).account_setter(self.national_id1)

    def client_info_setter(self):
        clients_book[self.client_id] = {
            'personal_info': {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'National_id': self.national_id1,
                'mobile_no': self.mobile
            },
            'account_info': {
                'account_id': self.account_id,
                'account_balance': self.balance,
                'account_type': self.type,
                'account_password': self.passowrd,
            }
        }

    def personal_display(self):
        print(f"Client Name is : {self.first_name} {self.last_name} ")
        print(f"Client national ID is : {self.national_id1}")
        print(f"Client national ID is : {self.mobile}")

    def mobile_setter(self, new_number):
        self.mobile = int(new_number)
        item['personal_info']['mobile_no'] = self.mobile


class Modifications(Client):

    def __init__(self, account_balance, account_password, account_type, mobile):
        self.balance = account_balance
        self.passowrd = account_password
        self.type = account_type
        self.mobile = mobile




running = True
used_sequence = []
new_client = ""
test11111 = 0
clients_book = {'client1': {'account_info': {'account_balance': 0,
                              'account_id': 1022821753,
                              'account_password': '0000',
                              'account_type': 'normal'},
             'personal_info': {'National_id': 1022818684,
                               'first_name': 'Saud',
                               'last_name': 'Alghamdi',
                               'mobile_no': 500053197}},
 'client2': {'account_info': {'account_balance': 0,
                              'account_id': 1066865284,
                              'account_password': '0000',
                              'account_type': 'normal'},
             'personal_info': {'National_id': 1066858745,
                               'first_name': 'Sana',
                               'last_name': 'Alghamdi',
                               'mobile_no': 533222025}}}

while running:
    choice = input("Enter the account number, '1' for creating new account, or '0' to stop the program :\n")
    # choices
    if choice == "1":
        i = len(used_sequence)+3
        if i not in used_sequence:
            add = True
            while add:
                national_id = int(input("ID Please: \n"))
                first_name = input('First name: \n').lower().capitalize()
                last_name = input('Last name: \n').lower().capitalize()
                mobile_no = int(input('mobile number: \n'))
                print(f"Person's name is: '{first_name} {last_name}', ID {national_id}, Phone number is: '{mobile_no}'\n")
                submit = input("Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()

                if submit == "y":
                    new_client += f"client{i}"
                    client_info = Client(new_client, national_id, first_name, last_name, mobile_no)
                    used_sequence.append(i)
                    client_info.client_info_setter()
                    new_client = ""
                    add = False

        client_info.account_display()
        client_info.personal_display()
        # pprint(clients_book)
    elif choice == "0":
        pprint(clients_book)
    else:
        test = 0
        for item in clients_book.items():
            if str(item[1]['account_info']['account_id']) == choice:
                item = item[1]
                # print(item)
                test = 3
                break
        if test == 0:
            print("Sorry that item is not available.")


        while test != 0:
            password = input('Enter your password: ')
            if password == item['account_info']['account_password']:
                current_client = Modifications(item['account_info']['account_balance'],
                                               item['account_info']['account_password'],
                                               item['account_info']['account_type'],
                                               item['personal_info']['mobile_no'])
                test = 0
            else:
                test -= 1
                print(f"Incorrect password, you still have {test} attempts ")

            choice = input("Enter '1' for Deposit:\n"
                           "Enter '2' for Withdraw:\n"
                           "Enter '3' for update Mobile No:\n"
                           "Enter '4' for Transactions Info:\n"
                           "Enter '5' for Account Info:\n")

        inside = True
        while inside:
            if choice == '1':
                choice = input("enter amount for deposit:\n")
                current_client.deposit_setter(choice)

            elif choice == '2':
                choice = input("enter amount to widthdeae:\n")
                current_client.withdraw_setter(choice)

            elif choice == '3':
                choice = input("enter new mobile no :\n")
                current_client.mobile_setter(choice)

            elif choice == '4':
                pass

            elif choice == '5':
                print(item)

            elif choice == '0':
                inside = False

            else:
                print("Invalid Entry, Try again")
