import pytest
from bank_account import BankAccount

@pytest.fixture
def initial_amount():
    return BankAccount(1000)

def test_bank_account_initial_balance(initial_amount):
    # amount = BankAccount(1000)
    assert initial_amount.get_balance() == 1000, "残高が正しくありません"

def test_withdraw_sufficient_balance(initial_amount):
    # amount = BankAccount(1000)
    initial_amount.withdraw(500)
    assert initial_amount.get_balance() == 500, "引き出し後の残高が間違っています"

def test_withdraw_negative_amount(initial_amount):
    # amount = BankAccount(1000)
    with pytest.raises(ValueError, match="引き出し額は正の値でなければなりません"):
        initial_amount.withdraw(-100)

def test_deposit_negative_amount(initial_amount):
    # amount = BankAccount(1000)
    with pytest.raises(ValueError, match="預金額は正の値でなければなりません"):
        initial_amount.deposit(-100)

