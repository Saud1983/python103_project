

class Onwer:

    def __init__(self, n_id, f_name, l_name, mobile):
        self.first_name = f_name
        self.last_name = l_name
        self.national_id = n_id
        self.mobile = mobile


class BankAccount(Onwer):

    def __init__(self, n_id, f_name, l_name, mobile, acc_id, acc_balance,  acc_type, acc_pass):
        super().__init__(n_id, f_name, l_name, mobile)
        self.account_id = acc_id
        self.balance = acc_balance
        self.type = acc_type
        self.passowrd = acc_pass




dict = {
    'saud':[1000000001,'Saud', 'Alghamdi', '0500050000', 10001, 0, 'normal', '0000'],
    'ali':[1000000002,'Ali', 'Aldossari', '0500050001', 10002, 0, 'normal', '0000'],
    'ahmed':[1000000003,'Ahmed', 'ALajmi', '0500050002', 10003, 0, 'normal', '0000'],
    'khalid':[1000000004,'Khalid', 'Alqahtani', '0500050003', 10004, 0, 'normal', '0000'],
    }

for v in dict.values():
    client = BankAccount(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7])
    print(client.national_id)
    print(client.first_name)
    print(client.last_name)
    print(client.mobile)
    print(client.account_id)
    print(client.balance)
    print(client.type)
    print(client.passowrd)
