import requests
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        """預金をする"""
        if amount <= 0:
            raise ValueError("預金額は正の値でなければなりません")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """引き出す"""
        if amount <= 0:
            raise ValueError("引き出し額は正の値でなければなりません")
        if amount > self.balance:
            raise ValueError("残高不足です")
        self.balance -= amount
        return self.balance

    def get_balance_in_currency(self, currency):

        response = requests.get(f"https://fakecurrencyapi.com/?base=USD&currency={currency}")
        if response.status_code == 200:
            rate = response.json()['rate']
            return self.balance * rate
        else:
            raise Exception("通貨変換サービスにアクセスできませんでした")

    def get_balance(self):
        """残高の取得"""
        return self.balance

