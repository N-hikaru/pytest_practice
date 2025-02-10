import pytest
from bank_account import BankAccount

def test_bank_account_initial_balance():
    amount = BankAccount(1000)
    assert amount.get_balance() == 1000, "残高が正しくありません"

def test_deposit_positive_amount():
    amount = BankAccount(0)
    amount.deposit(500)
    assert amount.get_balance() == 500, "預金残高が間違っています"

def test_withdraw_sufficient_balance():
    amount = BankAccount(1000)
    amount.withdraw(500)
    assert amount.get_balance() == 500, "引き出し後の残高が間違っています"

def test_withdraw_insufficient_balance():
    amount = BankAccount(500)
    with pytest.raises(ValueError, match="残高不足です"):
        amount.withdraw(501)

def test_withdraw_negative_amount():
    amount = BankAccount(1000)
    with pytest.raises(ValueError, match="引き出し額は正の値でなければなりません"):
        amount.withdraw(-100)

def test_deposit_negative_amount():
    amount = BankAccount(1000)
    with pytest.raises(ValueError, match="預金額は正の値でなければなりません"):
        amount.deposit(-100)

