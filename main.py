from random import randint
from pprint import pprint
from datetime import datetime


class BankAccount:
    """ This Class has no __init__, because it create a bank account based on Client class,
     this class initiate back account whenever a new client was created, this class has methods like
     account_display, deposit_setter, withdraw_setter, password_setter"""

    def account_setter(self, client_national_id):  # To pass the client national ID and use it for creating Bank Account
        self.account_id = client_national_id + randint(1000, 9999)  # Calculates the Account ID based on national ID
        self.balance = 0  # Set the balance equals 0 whenever a new account is created
        # the plan for account type to be used with special treatment when a client has more than 250,000, but not yet.
        self.type = 'normal'  # Set the account type to normal whenever a new account is created.
        self.password = '0000'  # Set the account password equals 0000 whenever a new account is created

    # this method only used at the creation of an account. BUT IT SHOULD BE USED IN OTHER CASES WHICH NOT.
    def account_display(self):  # This method is to show the account information after creating it only.
        print(f"Account ID is : {self.account_id} ")
        print(f"Account Balance is : {self.balance}")
        print(f"Account Password is : {self.password}")
        print(f"Account Type is : {self.type}")

    def deposit_setter(self, add):  # To add money to the account and print the transaction details
        # this line is to apply the change to the object it self, so it can accept another transaction without having
        # to logoff from the object and create it again
        self.balance = self.balance + int(add)
        # This line is to change the balance in the dictionary for that account.
        item['account_info']['account_balance'] = self.balance

        # THESE LINES SHOULD BE DONE IN A SPECIAL METHOD TO USE THAT METHOD TWICE INSTEAD OF CODING THIS 5 LINES AGAIN
        transaction_info = datetime.now()
        today_date = transaction_info.date().strftime('%d %m %Y')
        day_number = transaction_info.strftime('%w')
        transaction_time = transaction_info.time().strftime('%I:%M %p')
        print(f'تم ايداع {add} ريال لرصيدك البنكي في يوم '
              f'{ar_weekday[int(day_number)]} بتاريخ  {today_date} الساعه {transaction_time}')

    def withdraw_setter(self, deduct):  # To deduct money to the account and print the transaction details
        if self.balance >= int(deduct):  # To check whether or not the account is sufficient
            # this line is to apply the change to the object it self, so it can accept another transaction without
            # having to logoff from the object and create it again
            self.balance = self.balance - int(deduct)
            # This line is to change the balance in the dictionary for that account.
            item['account_info']['account_balance'] = self.balance

            # THESE LINES ARE IN deposit_setter AND SHOULDN'T BE LIKE THIS
            transaction_info = datetime.now()
            today_date = transaction_info.date().strftime('%d %m %Y')
            day_number = transaction_info.strftime('%w')
            transaction_time = transaction_info.time().strftime('%I:%M %p')
            print(f'تم خصم {deduct} ريال من رصيدك البنكي في يوم .'
                  f'{ar_weekday[int(day_number)]} بتاريخ  {today_date} الساعه {transaction_time}')
        else:
            print('Your account balance is not sufficient for this withdraw!!!')

    def password_setter(self, account_password):  # To change the account password
        #  there is a condition to confirm the old password before updating it, and that condition should be here

        # this line is to apply the change to the object it self, so it can accept another transaction without
        # having to logoff from the object and create it again
        self.account_password = account_password

        # This line is to change the password in the dictionary for that account.
        item['account_info']['account_password'] = self.account_password


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
                'account_password': self.password,
            }
        }

    def personal_display(self):
        print(f"Client Name is : {self.first_name} {self.last_name} ")
        print(f"Client national ID is : {self.national_id1}")
        print(f"Client Mobile Number is : {self.mobile}")

    def mobile_setter(self, new_number):
        self.mobile = int(new_number)
        item['personal_info']['mobile_no'] = self.mobile


class Modifications(Client):

    def __init__(self, account_balance, account_password, account_type, mobile):
        self.balance = account_balance
        self.password = account_password
        self.type = account_type
        self.mobile = mobile


running = True
used_sequence = []
new_client = ""
ar_weekday = ['الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت']
clients_book = {}
# clients_book = {'client1': {'account_info': {'account_balance': 0,
#                               'account_id': 1022821753,
#                               'account_password': '0000',
#                               'account_type': 'normal'},
#              'personal_info': {'National_id': 1022818684,
#                                'first_name': 'Khalid',
#                                'last_name': 'Waleed',
#                                'mobile_no': 500053197}},
#  'client2': {'account_info': {'account_balance': 0,
#                               'account_id': 1066865284,
#                               'account_password': '0000',
#                               'account_type': 'normal'},
#              'personal_info': {'National_id': 1066858745,
#                                'first_name': 'Ali',
#                                'last_name': 'Ahmed',
#                                'mobile_no': 533222025}}}
while running:
    choice = input("Enter the account number,"
                   " '1' for creating new account,"
                   " '2' for check the clients book"
                   " or '0' to stop the program :\n")
    # choices
    if choice == "1":
        i = len(used_sequence)+1
        if i not in used_sequence:
            review = True
            while review:
                national_id = int(input("ID Please: \n"))
                first_name = input('First name: \n').lower().capitalize()
                last_name = input('Last name: \n').lower().capitalize()
                mobile_no = int(input('mobile number: \n'))
                print(f"Person's name is: '{first_name} {last_name}', ID {national_id},"
                      f" Phone number is: '{mobile_no}'\n")
                submit = input("Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()

                if submit == "y":
                    new_client += f"client{i}"
                    client_info = Client(new_client, national_id, first_name, last_name, mobile_no)
                    used_sequence.append(i)
                    client_info.client_info_setter()
                    new_client = ""
                    review = False
                    client_info.account_display()
                    client_info.personal_display()
                    # pprint(clients_book)
    elif choice == "0":
        running = False
    elif choice == "2":
        pprint(clients_book)
    else:
        test = 0
        item = {}  # Declare here so it will not give warning that says (variable can be unidentified)
        for element in clients_book.items():
            if str(element[1]['account_info']['account_id']) == choice:
                item = element[1]
                # print(item)
                test = 3
                break
        if test == 0:
            print("Sorry that item is not available.")

        while test != 0:
            inside = False
            password = input('Enter your password: ')
            if password == item['account_info']['account_password']:
                current_client = Modifications(item['account_info']['account_balance'],
                                               item['account_info']['account_password'],
                                               item['account_info']['account_type'],
                                               item['personal_info']['mobile_no'])
                test = 0
                inside = True
                while inside:
                    choice = input("\nEnter '1' for Deposit:\n"
                                   "Enter '2' for Withdraw:\n"
                                   "Enter '3' for update Mobile No:\n"
                                   "Enter '4' for updating password:\n"
                                   "Enter '5' for Account Info:\n"
                                   "or\n"
                                   "Enter 0 to logoff:\n")
                    print('\n')
                    if choice == '1':
                        choice = input("enter amount for deposit:\n")
                        current_client.deposit_setter(choice)

                    elif choice == '2':
                        choice = input("enter amount to withdraw:\n")
                        current_client.withdraw_setter(choice)

                    elif choice == '3':
                        choice = input("enter new mobile no :\n")
                        current_client.mobile_setter(choice)

                    elif choice == '4':
                        choice = input("enter current password :\n")
                        confirmation = False
                        if choice == item['account_info']['account_password']:
                            while not confirmation:
                                new_password = input("enter a new password :\n")
                                confirm_password = input("enter the password again :\n")
                                if new_password == confirm_password:
                                    current_client.password_setter(new_password)
                                    confirmation = True
                                else:
                                    print(f"Incorrect confirmation, try again")
                        else:
                            print(f"Incorrect password, You are redirected to the main screen ")
                            inside = False

                    elif choice == '5':
                        # pprint(item)
                        for i in range(2):
                            if i == 0:
                                x = 'account_info'
                                print(f"Account ID is : {item[x]['account_id']}")
                                print(f"Account Balance is : {item[x]['account_balance']}")
                                print(f"Account Password is : {item[x]['account_password']}")
                                print(f"Account Type is : {item[x]['account_type']}")
                            else:
                                x = 'personal_info'
                                print(f"Client Name is : {item[x]['first_name']} {item[x]['last_name']}")
                                print(f"Client National ID is : {item[x]['National_id']}")
                                print(f"Client Mobile Number is : {item[x]['mobile_no']}")

                    elif choice == '0':
                        inside = False

                    else:
                        print("Invalid Entry, Try again")

            else:
                test -= 1
                print(f"Incorrect password, you still have {test} attempts ")
