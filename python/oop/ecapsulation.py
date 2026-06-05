"""
THE FOUR PILLARS OF OOP
Pillar 1: Encapsulation (Keeping things together)


Dependencies:
- Python 3.8+
- No external packages


Concepts Learned:
1. What is a Class?
2. Building Our First Class
3. The Four Pillars of OOP
"""

# Constants
SEPARATOR = "=" * 50
CURRENCY = "₦"


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.transactions = []


    def deposit(self, amount):
        """Add money"""
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"Deposit: +{CURRENCY}{amount}")
            print(f"✅ Deposited {CURRENCY}{amount}")
        else:
            print("❌ Amount must be positive")


    def withdraw(self, amount):
        """Withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(f"Withdrawal: -{CURRENCY}{amount}")
            print(f"✅ Withdrew {CURRENCY}{amount}")
        else:
            print("❌ Insufficient funds or invalid amount")

    def get_balance(self):
        """check balance"""
        return self.__balance

    def show_transactions(self):
        """Show transaction history"""
        print(f"\n Transaction for {self.owner}:")
        for t in self.transactions[-5:]:  # Last 5
            print(f"  {t}")
        print(f"Current balance: {CURRENCY}{self.__balance}")


if __name__ == "__main__":

    # Using the bank account
    account = BankAccount("Alice", 1000)

    # operations
    account.deposit(500)  
    account.withdraw(200)

    # account.__balance = 10000000 # ❌ ERROR! Can't access directly
    account.withdraw(2000)   # ❌ Fails (insufficient funds)

    account.show_transactions()