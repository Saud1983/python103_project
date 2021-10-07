
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


class Modifications(BankAccount):

    def __init__(self, account_id, account_balance, account_password, account_type, mobile):






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





running = True
used_sequence = []
new_client = ""
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
        pprint(clients_book)
    elif choice == "0":
        running = False
    else:
        test = 0
        for item in clients_book.items():
            if str(item[1]['account_info']['account_id']) == choice:
                item = item[1]
                print(item)
                test = 3
                break
        if test == 0:
            print("Sorry that item is not available.")


        while test != 0:
            password = input('Enter your password: ')
            if password == item['account_info']['account_password']:
                # chosen_account = item[]
                current_client = Modifications()
                test = 0
            else:
                test -= 1
                print(f"Incorrect password, you still have {test} attempts ")
