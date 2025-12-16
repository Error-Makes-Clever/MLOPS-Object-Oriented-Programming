class Atm:
    """ATM system with encapsulation"""
    __counter = 1
    
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.cid = Atm.__counter
        Atm.__counter += 1
    
    def get_balance(self):
        """Getter for private balance"""
        return self.__balance
    
    def set_balance(self, new_value):
        """Setter with validation"""
        if isinstance(new_value, int) and new_value >= 0:
            self.__balance = new_value
        else:
            print('Invalid balance amount')
    
    def create_pin(self, user_pin, initial_balance):
        """Create PIN and set initial balance"""
        self.pin = user_pin
        self.__balance = initial_balance
        print('PIN created successfully')
    
    def change_pin(self, old_pin, new_pin):
        """Change PIN with validation"""
        if old_pin == self.pin:
            self.pin = new_pin
            print('PIN changed successfully')
        else:
            print('Incorrect old PIN')
    
    def check_balance(self, user_pin):
        """Check balance with PIN verification"""
        if user_pin == self.pin:
            print(f'Your balance is: ${self.__balance}')
        else:
            print('Incorrect PIN')
    
    def withdraw(self, user_pin, amount):
        """Withdraw with PIN and balance verification"""
        if user_pin != self.pin:
            print('Incorrect PIN')
            return
        
        if amount <= 0:
            print('Invalid amount')
            return
        
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrawal successful. Balance: ${self.__balance}')
        else:
            print('Insufficient funds')
    
    @staticmethod
    def get_counter():
        return Atm.__counter

# Usage
atm1 = Atm()
atm1.create_pin('1234', 1000)
atm1.check_balance('1234')  # Your balance is: $1000
atm1.withdraw('1234', 200)  # Withdrawal successful
atm1.check_balance('1234')  # Your balance is: $800