# ============================================================================
# SIMPLE INHERITANCE EXAMPLE (Commented Out)
# ============================================================================

# Base class (Parent class)
class Animal:
    """
    Base class representing a generic animal.
    This serves as the parent class from which other specific animals inherit.
    """
    def __init__(self, name):
        """
        Constructor that initializes the animal with a name.
        Logic: Stores the name attribute for the animal instance.
        """
        self.name = name

    def speak(self):
        """
        Generic speak method for all animals.
        Logic: Prints a generic sound message using the animal's name.
        """
        print(f"{self.name} makes a sound.")

# Derived class (Child class)
class Dog(Animal):
    """
    Derived class that inherits from Animal.
    Logic: 
    - Dog inherits all attributes and methods from Animal
    - Demonstrates method overriding by redefining speak()
    """

    def speak(self):
        """
        Overridden speak method specific to Dog.
        Logic: 
        - Replaces the parent class's speak() method
        - Provides dog-specific behavior (barking)
        - This is an example of polymorphism
        """
        print(f"{self.name} barks.")

# Create an instance of Animal
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound.

# Create an instance of Dog
# Logic: Dog inherits __init__ from Animal, so it expects a 'name' parameter
try:
    dog = Dog()  # Note: This would cause an error - missing required 'name' argument
    dog.speak()  # Output: Buddy barks.
except Exception as e:
    print("Error due Method Overriding :", e)

# ============================================================================
# SUPER KEYWORD DEMONSTRATION
# ============================================================================

# Base class (Parent class)
class Animal:
    """
    Base class representing a generic animal.
    Demonstrates initialization without parameters (hardcoded name).
    """
    def __init__(self):
        """
        Constructor that initializes with a default name.
        Logic: Sets a default name "Buddy" for all Animal instances.
        """
        self.name = "Buddy"

    def speak(self):
        """
        Generic speak method for all animals.
        Logic: Prints a generic sound message.
        This method will be called from the derived class using super().
        """
        print(f"{self.name} makes a sound.")

# # Derived class (Child class)
class Dog(Animal):
    """
    Derived class that inherits from Animal.
    Demonstrates proper use of super() keyword for:
    1. Calling parent class constructor
    2. Calling parent class methods
    """
    def __init__(self, breed):
        """
        Constructor that extends the parent class initialization.
        Logic:
        - super().__init__() calls the parent Animal's __init__()
        - This ensures the parent's initialization code runs first
        - Then adds an additional attribute 'breed' specific to Dog
        - This demonstrates proper inheritance chain initialization
        """
        super().__init__()  # Call parent class constructor to set self.name
        self.breed = breed  # Add Dog-specific attribute

    def speak(self):
        """
        Overridden speak method that extends parent functionality.
        Logic:
        - super().speak() calls the parent Animal's speak() method first
        - Then adds additional Dog-specific behavior
        - This demonstrates method extension (not just replacement)
        - Allows reusing parent code while adding new functionality
        """
        super().speak()  # Call the base class speak() method
        print(f"{self.name} barks. It is a {self.breed}.")

# # Create an instance of Dog
"""
Execution flow:
1. Dog("Golden Retriever") is called
2. Dog's __init__ runs:
   - super().__init__() calls Animal's __init__()
   - Animal's __init__ sets self.name = "Buddy"
   - Dog's __init__ then sets self.breed = "Golden Retriever"
3. dog.speak() is called
4. Dog's speak() runs:
   - super().speak() calls Animal's speak() -> prints "Buddy makes a sound."
   - Then executes Dog's additional code -> prints "Buddy barks. It is a Golden Retriever."
"""
dog = Dog("Golden Retriever")
dog.speak()

# Output:
# Buddy makes a sound.          <- From Animal's speak() via super().speak()
# Buddy barks. It is a Golden Retriever.  <- From Dog's speak() additional code


# ============================================================================
# KEY CONCEPTS EXPLAINED
# ============================================================================

"""
1. INHERITANCE:
   - Dog inherits from Animal using class Dog(Animal)
   - Dog automatically gets all attributes and methods from Animal
   - Child class can access parent's self.name without redefining it

2. METHOD OVERRIDING:
   - Dog redefines speak() method (present in both Animal and Dog)
   - When dog.speak() is called, Python uses Dog's version (child overrides parent)
   
3. SUPER() KEYWORD:
   - super().__init__() calls the parent class constructor
   - super().speak() calls the parent class method
   - Allows child class to extend (not just replace) parent functionality
   - Maintains proper initialization chain in inheritance hierarchy
   
4. WHY USE SUPER():
   - Avoids code duplication (reuse parent's initialization/methods)
   - Maintains single source of truth for parent functionality
   - Makes code more maintainable (changes in parent auto-reflect in children)
   - Supports multiple inheritance properly (though not shown here)

5. EXECUTION ORDER WITH SUPER():
   - Child's method runs
   - When super() is called, execution jumps to parent's method
   - Parent's method completes
   - Execution returns to child's method and continues
"""