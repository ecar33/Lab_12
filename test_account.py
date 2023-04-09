import pytest

from account import *

def test_init():
    test_account_1 = Account("Steve")
    assert test_account_1.account_balance == 0
    assert test_account_1.account_name == "Steve"
    test_account_2 = Account(0)
    assert test_account_2.account_balance == 0
    assert test_account_2.account_name == 0
def test_deposit():
    account = Account("test")
    assert account.deposit(0) == True
    assert account.deposit("test") == False
    assert account.deposit(3.1414141414) == True
    assert account.get_balance() == 3.1414141414
    assert account.deposit(-1) == False
    assert account.deposit(9999999999) == True
    assert account.get_balance() == pytest.approx(10000000002.14, .01)
    assert account.deposit('') == False

def test_withdraw():
    account = Account("test")
    assert account.deposit(30) == True
    assert account.get_balance() == 30
    assert account.withdraw("test") == False
    assert account.get_balance() == 30
    assert account.withdraw(10) == True
    assert account.get_balance() == 20
    assert account.deposit(-1) == False
    assert account.get_balance() == 20
    assert account.withdraw('') == False
    assert account.get_balance() == 20
    assert account.withdraw(20) == True
    assert account.get_balance() == 0
    assert account.withdraw(20) == False
    assert account.get_balance() == 0





