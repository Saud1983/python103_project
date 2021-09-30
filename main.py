class Onwer:

    def __init__(self, national_id, f_name, l_name, mobile):
        self._first_name = f_name
        self._last_name = l_name
        self.__id = national_id
        self._mobile = mobile


class BankAccount:

    def __init__(self, acc_id, acc_balance,  acc_type, acc_pass):
        self.__account_id = acc_id
        self.__balance = acc_balance
        self.__type = acc_type
        self.__passowrd = acc_pass
