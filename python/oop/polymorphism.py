"""
PART 3: THE FOUR PILLARS OF OOP
Pillar 3: Polymorphism (Many forms)  

Dependencies:
- Python 3.8+
- No external packages

"""

# Constants
SEPARATOR = "=" * 50
CURRENCY = "₦"


class PaymentMethod:
    def __init__(self, owner):
        self.owner = owner

    def pay(self, amount):
        """Process payment - to be overridden"""
        pass

    def receipt(self):
        """Generate receipt"""
        return f"Payment from {self.owner}"


class CreditCard(PaymentMethod):
    def __init__(self, owner, card_number, expiry):
        super().__init__(owner)
        self.card_number = card_number[-4:]
        self.expiry = expiry


    def pay(self, amount):
        print(f"💳 Charging {CURRENCY}{amount} to card ending in {self.card_number}")
        return True

    def receipt(self):
        return f"Credit Card ({self.card_number}) - {super().receipt()}"


class Cash(PaymentMethod):
    def __init__(self, owner, cash_given):
        super().__init__(owner)
        self.cash_given = cash_given

    def pay(self, amount):
        if self.cash_given >= amount:
            change = self.cash_given - amount
            print(f"💵 Paid {CURRENCY}{amount} in cash. change Change: {CURRENCY}{change:.2f}")
            return True
        else:
            print(f"❌ Insufficient cash. Need {CURRENCY}{amount - self.cash_given:.2f} more")
            return False

    def receipt(self):
        return f"Cash - {super().receipt()}"


class Crypto(PaymentMethod):
    def __init__(self, owner, wallet_address):
        super().__init__(owner)
        self.wallet_address = wallet_address[:6] + "..."

    def pay(self, amount):
        print(f"🪙 Transferring {amount/50000:.4f} BTC from {self.wallet_address}")
        return True

    def receipt(self):
        return f"Crypto ({self.wallet_address}) - {super().receipt()}"

def main():
    # Polymorphism in action - same method, different behavior!
    def process_payment(payment_method, amount):
        """Works with ANY payment method!"""
        print(f"\nProcessing {CURRENCY}{amount} payment...")
        if payment_method.pay(amount):
            print(f"✅ Success! {payment_method.receipt()}")
        else:
            print("❌ Payment failed")

    # Different payment methods
    process_payment(CreditCard("Ada", "1233778473993098", "12/25"), 70000)
    process_payment(Cash("John", 80000), 60000)
    process_payment(Crypto("Abel", "1A1zPle88JUfiUWye33002IINba"), 136000)


if __name__ == "__main__":
    main()
