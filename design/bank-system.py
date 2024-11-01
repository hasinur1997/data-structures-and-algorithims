class Bank:

    def __init__(self, balance):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False

        width_draw = self.withdraw(account1, money)

        if not width_draw:
            return False

        self.deposit(account2, money)

        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False

        self.balance[account-1] = self.balance[account-1] + money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False

        current_balance = self.balance[account-1]

        if money > current_balance:
            return False

        self.balance[account - 1] = current_balance - money

        return True

    def _is_valid_account(self, account_number):
        account_number = account_number - 1
        return account_number < len(self.balance)



bank = Bank([10, 100, 20, 50, 30])

print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))

print(bank.balance)
