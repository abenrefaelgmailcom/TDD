import pytest
from bank_account import BankAccount


def test_new_account_starts_with_zero_balance():
    # create new account
    account = BankAccount()

    # check initial balance
    assert account.get_balance() == 0


def test_deposit_money_once():
    account = BankAccount()

    account.deposit(100)

    assert account.get_balance() == 100


def test_deposit_money_twice():
    account = BankAccount()

    account.deposit(100)
    account.deposit(50)

    assert account.get_balance() == 150


def test_withdraw_money():
    account = BankAccount()

    account.deposit(100)
    account.withdraw(30)

    assert account.get_balance() == 70


def test_balance_after_deposit_and_withdraw():
    account = BankAccount()

    account.deposit(200)
    account.withdraw(50)
    account.deposit(25)

    assert account.get_balance() == 175


def test_is_empty_returns_true_for_new_account():
    account = BankAccount()

    assert account.is_empty() is True


def test_is_empty_returns_false_after_deposit():
    account = BankAccount()

    account.deposit(10)

    assert account.is_empty() is False