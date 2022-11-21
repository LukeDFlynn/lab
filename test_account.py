import pytest
from account import *

class Test:


    def setup_method(self):
        self.account_one = Account('John')
        self.account_two = Account('Jim')

    def teardown_method(self):
        del self.account_one
        del self.account_two

    def test_init(self):
        assert self.account_one.get_name() == 'John'
        assert self.account_two.get_name() == 'Jim'

    def test_deposit(self):
        assert self.account_one.deposit(5) is True
        assert self.account_one.deposit(-16) is False
        assert self.account_two.deposit(53) is True
        assert self.account_two.deposit(-4) is False

    def test_withdraw(self):
        assert self.account_one.withdraw(5) is False
        assert self.account_one.withdraw(-17) is False
        assert self.account_two.withdraw(600) is False
        assert self.account_two.withdraw(-32) is False



