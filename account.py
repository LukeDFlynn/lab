class Account:

    def __init__(self, name):

        self.__account_name = None
        self.__account_balance = 0

    def deposit(self, amount):

        '''
        :param amount: amount
        :return: True
        '''
        if amount != 0 and amount.isPositive():
            self.__account_balance += amount
        else:
            return False

    def withdraw(self, amount):
        '''
        :param amount: amount
        :return: True
        '''
        if amount != 0 and amount.isPositive() and amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

