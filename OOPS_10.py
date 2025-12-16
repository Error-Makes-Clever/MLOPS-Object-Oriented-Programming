class Address:
    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state
    
    def get_city(self):
        return self.__city
    
    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address  # Has-A relationship
    
    def print_address(self):
        print(f"{self.address.get_city()}, "
              f"{self.address.pin}, "
              f"{self.address.state}")
    
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)

# Create Address object
add1 = Address('Gurgaon', 122011, 'Haryana')

# Create Customer with Address
cust = Customer('Nitish', 'male', add1)
cust.print_address()  # Gurgaon, 122011, Haryana

# Edit through Customer
cust.edit_profile('Ankit', 'Mumbai', 111111, 'Maharashtra')
cust.print_address()  # Mumbai, 111111, Maharashtra