
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # Encapsulation (private)

    # Abstraction: User calls this without caring how it works internally
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited.")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn.")

    # Encapsulation: controlled access to balance
    def get_balance(self):
        return self.__balance
    


kofi_account = Account("Kofi", 50)

kofi_account.deposit(770)

kofi_balance = kofi_account.get_balance() 

print(f"Kofi's balance is ${kofi_balance}.00") # $820.00


