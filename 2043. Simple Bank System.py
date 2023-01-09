class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.checkAccount(account1, account2):
            if self.balance[account1-1] >= money:
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if self.checkAccount(account):
            self.balance[account-1] += money
            return True 
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.checkAccount(account):
             if self.balance[account-1] >= money:
                 self.balance[account-1] -= money
                 return True 
        return False

    def checkAccount(self, account1: int, account2: int = 1) -> bool:
        return account1 >=  1 and account2 >= 1 and account1 <= self.n and account2 <= self.n
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
