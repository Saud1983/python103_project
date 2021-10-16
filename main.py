from random import randint
from pprint import pprint
from datetime import datetime


class BankAccount:
    """ This Class creates a bank account based on Client class, this class supposed to initiate a bank account
    whenever a new client was created, this class has methods like
     account_display, deposit_setter, withdraw_setter, password_setter"""

    # I used default values for this init method because I have tow different scenarios.

    # One is calling this class for creating a new account, and that will use the default values to create the object
    # then will go to account_setter to give the official values for that created account.

    # The other scenario is when calling this class for retrieving account data that already exists, and for that
    # the init method will use the real data that has been passed to it.
    def __init__(self, account_id=0, account_balance=0, account_type=0, account_password=0):
        self.account_id = account_id
        self.account_balance = account_balance
        self.account_type = account_type
        self.account_password = account_password

    def account_setter(self, national_id):  # To pass the client national ID and use it for creating Bank Account
        self.account_id = national_id + randint(1000, 9999)  # Calculates the Account ID based on national ID
        self.account_balance = 0  # Set the balance equals 0 whenever a new account is created

        # the plan for account type to be used with special treatment when a client has more than 250,000, but not yet.
        self.account_type = 'normal'  # Set the account type to normal whenever a new account is created.
        self.account_password = '0000'  # Set the account password equals 0000 whenever a new account is created

    # this method only used at the creation of an account. BUT IT SHOULD BE USED IN OTHER CASES WHICH NOT.
    def account_display(self):  # This method is to show the account information after creating it only.
        print(f"Account ID is : {self.account_id} ")
        print(f"Account Balance is : {self.account_balance}")
        print(f"Account Password is : {self.account_password}")
        print(f"Account Type is : {self.account_type}")

    def deposit_setter(self, add):  # To add money to the account and print the transaction details
        # this line is to apply the change to the object it self, so it can accept another transaction without having
        # to logoff from the object and create it again
        self.account_balance = self.account_balance + int(add)
        # This line is to change the balance in the dictionary for that account.
        item['account_info']['account_balance'] = self.account_balance

        # THESE LINES SHOULD BE DONE IN A SPECIAL METHOD TO USE THAT METHOD TWICE INSTEAD OF CODING THIS 5 LINES AGAIN
        transaction_info = datetime.now()
        today_date = transaction_info.date().strftime('%d %m %Y')
        day_number = transaction_info.strftime('%w')
        transaction_time = transaction_info.time().strftime('%I:%M %p')
        print(f'تم ايداع {add} ريال لرصيدك البنكي في يوم '
              f'{ar_weekday[int(day_number)]} بتاريخ  {today_date} الساعه {transaction_time}')

    def withdraw_setter(self, deduct):  # To deduct money to the account and print the transaction details
        if self.account_balance >= int(deduct):  # To check whether or not the account is sufficient
            # this line is to apply the change to the object it self, so it can accept another transaction without
            # having to logoff from the object and create it again
            self.account_balance = self.account_balance - int(deduct)
            # This line is to change the balance in the dictionary for that account.
            item['account_info']['account_balance'] = self.account_balance

            # THESE LINES ARE IN deposit_setter AND SHOULDN'T BE LIKE THIS
            transaction_info = datetime.now()
            today_date = transaction_info.date().strftime('%d %m %Y')
            day_number = transaction_info.strftime('%w')
            transaction_time = transaction_info.time().strftime('%I:%M %p')
            print(f'تم خصم {deduct} ريال من رصيدك البنكي في يوم .'
                  f'{ar_weekday[int(day_number)]} بتاريخ  {today_date} الساعه {transaction_time}')
        else:
            print('Your account balance is not sufficient for this withdraw!!!')

    def password_setter(self):  # To change the account password
        old_password = input("enter current password :\n")  # To make sure that the user is the client
        confirmation = False  # For the next while loop
        if old_password == item['account_info']['account_password']:  # If the password is correct
            while not confirmation:  # Start a loop of giving the new password twice
                new_password = input("enter a new password :\n")
                confirm_password = input("enter the password again :\n")
                if new_password == confirm_password:
                    # this line is to apply the change to the object it self, so it can accept another transaction
                    # without having to logoff from the object and create it again
                    self.account_password = new_password

                    # This line is to change the password in the dictionary for that account.
                    item['account_info']['account_password'] = self.account_password
                    return True  # This is because I need to return a boolean value for continuing in the client menu
                else:
                    print(f"Incorrect confirmation, try again")
        else:
            print(f"Incorrect password, You are redirected to the main screen ")
            return False  # to leave the client account entirely


class Client(BankAccount):
    """This class is the responsible for creating new clients + associated account at once, it also has some other
     methods such as personal_display and mobile_setter"""

    #  The initiation method for a new client, and calling the BankAccount Class for creating the account
    def __init__(self, client_id="", national_id=0, first_name="", last_name="", mobile=0):
        BankAccount.__init__(self)  # Just to remove the warning
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.mobile = mobile
        super(Client, self).account_setter(self.national_id)  # To create the account based on the client national ID

    #  This method is to save the current created object to a dictionary before using the same object for a new creation
    def client_info_setter(self):
        clients_book[self.client_id] = {
            'personal_info': {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'National_id': self.national_id,
                'mobile_no': self.mobile
            },
            'account_info': {
                'account_id': self.account_id,
                'account_balance': self.account_balance,
                'account_type': self.account_type,
                'account_password': self.account_password,
            }
        }

    # this method only used at the creation of a client. BUT IT SHOULD BE USED IN OTHER CASES WHICH NOT.
    def personal_display(self):  # This method is to show the client information after creating it only.
        print(f"Client Name is : {self.first_name} {self.last_name} ")
        print(f"Client national ID is : {self.national_id}")
        print(f"Client Mobile Number is : {self.mobile}")

    def mobile_setter(self, new_number):  # To change the client mobile number
        self.mobile = int(new_number)
        item['personal_info']['mobile_no'] = self.mobile


class Modifications(Client):
    """This class is to create a temporary object that can retrieve account/client data from client_book dictionary
    so it can modify some information using methods from BankAccount, Client classes """

    def __init__(self, account_id, account_balance, account_password, account_type, nation_id, f_name, l_name, mobile):
        Client.__init__(self)  # Just to remove the warning
        self.account_id = account_id
        self.account_balance = account_balance
        self.account_password = account_password
        self.account_type = account_type
        self.national_id = nation_id
        self.first_name = f_name
        self.last_name = l_name
        self.mobile = mobile


running = True  # The boolean variable that used by the main while loop of this program
used_sequence = []  # A serial number list that contains a suffix number of newly created client. Ex client1, client2,..
new_client = ""  # A string that should contains the word "client" + a number that's not in used_sequence list
ar_weekday = ['الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت']  # Used in a transaction details
# clients_book = {}  # It's the database that contains all clients details

# Next dictionary is an example with tow clients info that can be used instead of the empty clients_book dictionary
clients_book = {'client-1': {'account_info': {'account_balance': 0,
                                              'account_id': 1022821753,
                                              'account_password': '0000',
                                              'account_type': 'normal'},
                             'personal_info': {'National_id': 1022818684,
                                               'first_name': 'Khalid',
                                               'last_name': 'Waleed',
                                               'mobile_no': 500053197}},
                'client-2': {'account_info': {'account_balance': 0,
                                              'account_id': 1066865284,
                                              'account_password': '0000',
                                              'account_type': 'normal'},
                             'personal_info': {'National_id': 1066858745,
                                               'first_name': 'Ali',
                                               'last_name': 'Ahmed',
                                               'mobile_no': 533222025}}}


while running:  # Program starts here.
    choice = input("Enter the account number,"
                   " '1' for creating new account,"
                   " '2' for check the clients book"
                   " or '0' to stop the program :\n")
    # choices
    if choice == "1":  # 1st choice
        i = len(used_sequence)+1  # This variable to make sure that the selected number is not in used_sequence

        if i not in used_sequence:
            review = True  # For the second while loop
            while review:  # Start adding new client info

                # These next 4 lines can be shortened by using Regex
                cl_n_id = int(input("ID Please: \n"))
                cl_f_name = input('First name: \n').lower().capitalize()
                cl_l_name = input('Last name: \n').lower().capitalize()
                cl_mobile = int(input('mobile number: \n'))

                # Review the new client info
                print(f"Person's name is: '{cl_f_name} {cl_l_name}', ID {cl_n_id},"
                      f" Phone number is: '{cl_mobile}'\n")
                submit = input("Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()

                if submit == "y":
                    new_client += f"client{i}"  # The key for a sub-dictionary that represents the value of that key
                    client_info = Client(new_client, cl_n_id, cl_f_name, cl_l_name, cl_mobile)  # Create an object
                    used_sequence.append(i)  # Add this number to used_sequence so it will not be used again
                    client_info.client_info_setter()  # Add the new client info to a clients_book using a setter method
                    new_client = ""  # Empty the variable to be used again with new word 'client' with a unique number
                    client_info.account_display()  # Call a method to display the new client account info
                    client_info.personal_display()  # Call a method to display the new client personal info
                    review = False  # Terminate the while loop

    elif choice == "0":  # 2nd choice
        running = False  # To stop the program

    elif choice == "2":  # 3rd choice
        pprint(clients_book)  # To print the whole book of clients and their information

    else:  # Last choice To retrieve a client by its account number for making some transactions
        attempts = 0  # Declare here so it will not give warning that says (variable can be unidentified)
        item = {}  # Declare here so it will not give warning that says (variable can be unidentified)
        for element in clients_book.items():
            if str(element[1]['account_info']['account_id']) == choice:  # Here the choice can be an account number
                item = element[1]  # This is a sub-dictionary from the clients_book contains client/account info
                # print(item)
                attempts = 3  # Give the user 3 attempts to enter the password correctly
                break  # stop the for loop after finding the account number

        if attempts == 0:  # If the account number in not the the clients_book print the message
            print("Sorry that item is not available.")

        while attempts != 0:  # If the account has been found this line will work
            password = input('Enter your password: ')
            if password == item['account_info']['account_password']:
                # Create an object contains the data for that selected account
                current_client = Modifications(item['account_info']['account_id'],
                                               item['account_info']['account_balance'],
                                               item['account_info']['account_password'],
                                               item['account_info']['account_type'],
                                               item['personal_info']['National_id'],
                                               item['personal_info']['first_name'],
                                               item['personal_info']['last_name'],
                                               item['personal_info']['mobile_no'])
                attempts = 0  # To make sure that the upper while loop can not run without a correct account id
                inside = True  # This is for the next loop that designed for a client special menu
                while inside:  # Start client menu here
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
                        current_client.deposit_setter(choice)  # To add money

                    elif choice == '2':
                        choice = input("enter amount to withdraw:\n")
                        current_client.withdraw_setter(choice)  # To deduct money

                    elif choice == '3':
                        choice = input("enter new mobile no :\n")
                        current_client.mobile_setter(choice)  # To modify the client mobile number

                    elif choice == '4':
                        value = current_client.password_setter()
                        if not value:
                            inside = value  # to leave the client account entirely

                    elif choice == '5':  # To print the client info
                        current_client.account_display()
                        current_client.personal_display()

                    elif choice == '0':  # To leave and close the account
                        inside = False

                    else:  # For unexpected entry from the user
                        print("Invalid Entry, Try again")

            else:  # If the client entered a wrong password
                attempts -= 1  # The attempts will be reduced by one
                print(f"Incorrect password, you still have {attempts} attempts ")
