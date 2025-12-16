from abc import ABC, abstractmethod

class BankApp(ABC):
    """Abstract base class"""
    
    def database(self):
        """Concrete method - implemented"""
        print("Connected to database")
    
    @abstractmethod
    def security(self):
        """Abstract method - must be implemented by subclass"""
        pass
    
    @abstractmethod
    def display(self):
        """Abstract method - must be implemented by subclass"""
        pass

# This will cause error - cannot instantiate abstract class
# obj = BankApp()  # TypeError!

try:
    obj = BankApp()
except TypeError as e:
    print(e)

class MobileApp(BankApp):
    """Concrete class implementing abstract methods"""
    
    def security(self):
        print("Mobile security layer")
    
    def display(self):
        print("Mobile display interface")
    
    def mobile_login(self):
        print("Mobile login")

# Now we can create instance
app = MobileApp()
app.database()       # Inherited concrete method
app.security()       # Implemented abstract method
app.display()        # Implemented abstract method
app.mobile_login()   # Own method