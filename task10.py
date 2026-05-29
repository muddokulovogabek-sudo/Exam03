class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balansga {amount} qo‘shildi. Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Pul yetarli emas")
        else:
            self.balance -= amount
            print(f"{amount} yechildi. Qolgan balans: {self.balance}")
            object