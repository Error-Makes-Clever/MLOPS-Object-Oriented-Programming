# ============================================================================
# 1. SINGLE (BASIC) INHERITANCE
# ============================================================================
"""
Single Inheritance: One child class inherits from one parent class.
Structure: Parent -> Child (linear inheritance chain)
"""

# Base class (Parent class)
class Parent:
    """
    Base class representing a parent.
    Logic: Provides basic attributes and methods that child can inherit.
    """
    def __init__(self, name):
        """
        Constructor to initialize parent with a name.
        Logic: This will be inherited by Child, so Child instances will also have 'name'.
        """
        self.name = name

    def greet(self):
        """
        Method to greet.
        Logic: Child class inherits this method without redefining it.
        """
        print(f"Hello, my name is {self.name}.")

# Derived class (Child class)
class Child(Parent):
    """
    Child class that inherits from Parent.
    Logic:
    - Inherits __init__ and greet() from Parent automatically
    - Adds its own method play() for child-specific behavior
    - Does not override any parent methods (pure extension)
    """

    def play(self):
        """
        Child-specific method.
        Logic: Adds new functionality without modifying parent behavior.
        """
        print(f"{self.name} is playing.")

# Create an instance of Child
# Execution flow: Child("Alice") -> Parent.__init__("Alice") sets self.name = "Alice"
child = Child("Alice")
child.greet()  # Calls inherited method from Parent
               # Output: Hello, my name is Alice.
child.play()   # Calls Child's own method
               # Output: Alice is playing.

# ------------------------------------------------------------

# ============================================================================
# 2. MULTILEVEL INHERITANCE
# ============================================================================
"""
Multilevel Inheritance: Classes inherit in a chain (grandparent -> parent -> child).
Structure: Grandparent -> Parent -> Child (multi-level chain)
Each level adds functionality while inheriting from above.
"""

# Base class (Level 1)
class Grandparent:
    """
    Top-level base class in the inheritance chain.
    Logic: Foundation class that starts the inheritance hierarchy.
    """
    def __init__(self, name):
        """
        Constructor for grandparent.
        Logic: This initialization will cascade down through all child classes.
        """
        self.name = name

    def tell_story(self):
        """
        Grandparent-specific method.
        Logic: Available to all descendants in the chain.
        """
        print(f"{self.name} tells a story.")

# Intermediate class (Level 2)
class Parent(Grandparent):
    """
    Intermediate class that inherits from Grandparent.
    Logic:
    - Inherits __init__ and tell_story() from Grandparent
    - Adds work() method
    - Acts as both child (of Grandparent) and parent (of Child)
    """

    def work(self):
        """
        Parent-specific method.
        Logic: Adds intermediate-level functionality.
        """
        print(f"{self.name} is working.")

# Derived class (Level 3)
class Child(Parent):
    """
    Final derived class in the chain.
    Logic:
    - Inherits from Parent (which already inherits from Grandparent)
    - Has access to ALL methods: tell_story(), work(), and play()
    - Demonstrates transitive inheritance (inherits from grandparent through parent)
    """

    def play(self):
        """
        Child-specific method.
        Logic: Adds the final level of functionality.
        """
        print(f"{self.name} is playing.")

# Create an instance of Child
# Inheritance chain: Child -> Parent -> Grandparent
child = Child("Charlie")
child.tell_story()  # From Grandparent (2 levels up)
                    # Output: Charlie tells a story.
child.work()        # From Parent (1 level up)
                    # Output: Charlie is working.
child.play()        # From Child (own method)
                    # Output: Charlie is playing.

# ------------------------------------------------------------

# ============================================================================
# 3. HIERARCHICAL INHERITANCE
# ============================================================================
"""
Hierarchical Inheritance: Multiple child classes inherit from one parent.
Structure: 
           Parent
          /      \
      Child1    Child2
One parent, multiple children (siblings don't inherit from each other).
"""

# Base class
class Parent:
    """
    Common parent class for multiple children.
    Logic: Shared functionality for all child classes.
    """
    def __init__(self, name):
        """
        Constructor shared by all children.
        Logic: Both Child1 and Child2 will inherit this initialization.
        """
        self.name = name

    def greet(self):
        """
        Common method inherited by all children.
        Logic: Shared behavior across all child classes.
        """
        print(f"Hello, my name is {self.name}.")

# Derived class 1
class Child1(Parent):
    """
    First child class.
    Logic:
    - Inherits from Parent
    - Sibling to Child2 (no relationship between them)
    - Has unique play() method
    """

    def play(self):
        """
        Child1-specific behavior.
        Logic: Only available to Child1 instances.
        """
        print(f"{self.name} is playing.")

# Derived class 2
class Child2(Parent):
    """
    Second child class.
    Logic:
    - Also inherits from Parent independently
    - Sibling to Child1 (no access to Child1's methods)
    - Has unique study() method
    """

    def study(self):
        """
        Child2-specific behavior.
        Logic: Only available to Child2 instances.
        """
        print(f"{self.name} is studying.")

# Create instances of Child1 and Child2
child1 = Child1("Dave")
child2 = Child2("Eve")

# Both children can use parent's method
child1.greet()  # Output: Hello, my name is Dave.
child1.play()   # Child1's unique method
                # Output: Dave is playing.

child2.greet()  # Output: Hello, my name is Eve.
child2.study()  # Child2's unique method
                # Output: Eve is studying.

# Note: child1.study() would cause AttributeError (siblings don't share methods)
# Note: child2.play() would cause AttributeError

# ------------------------------------------------------------

# ============================================================================
# 4. MULTIPLE INHERITANCE (DIAMOND PROBLEM)
# ============================================================================
"""
Multiple Inheritance: A class inherits from multiple parent classes.
Diamond Problem: When a class inherits from two classes that share a common ancestor.
Structure:
        A
       / \
      B   C
       \ /
        D
Python uses MRO (Method Resolution Order) to resolve which method to call.
MRO follows C3 Linearization algorithm: depth-first, left-to-right.
"""

# Common base class (Top of diamond)
class A:
    """
    Common ancestor in the diamond inheritance pattern.
    Logic: Base class that both B and C inherit from.
    """
    def __init__(self, name):
        """
        Base constructor.
        Logic: Will be called last in the MRO chain.
        """
        self.name = name

    def greet(self):
        """
        Base greet method.
        Logic: Final method in the super() chain.
        """
        print(f"Hello from A, {self.name}.")

# Intermediate class 1 (Left side of diamond)
class B(A):
    """
    First intermediate class inheriting from A.
    Logic: Part of the diamond pattern, uses super() to maintain MRO chain.
    """

    def greet(self):
        """
        B's greet method.
        Logic:
        - Overrides A's greet
        - Calls super().greet() to continue the MRO chain
        - super() will call C's greet (next in MRO), NOT A's greet directly
        """
        print(f"Hello from B, {self.name}.")
        # super().greet()  # Continues MRO chain (calls C.greet in this case)

# Intermediate class 2 (Right side of diamond)
class C(A):
    """
    Second intermediate class inheriting from A.
    Logic: Part of the diamond pattern, uses super() to maintain MRO chain.
    """
    def greet(self):
        """
        C's greet method.
        Logic:
        - Overrides A's greet
        - Calls super().greet() to continue the MRO chain
        - super() will call A's greet (next in MRO)
        """
        print(f"Hello from C, {self.name}.")
        # super().greet()  # Continues MRO chain (calls A.greet)

# Derived class (Bottom of diamond)
class D(B, C):
    """
    Final class that inherits from both B and C (multiple inheritance).
    Logic:
    - Inherits from both B and C (which both inherit from A)
    - Creates diamond pattern: A is inherited through two paths
    - MRO for D: D -> B -> C -> A -> object
    - Order matters: D(B, C) vs D(C, B) gives different MRO
    """

    def greet(self):
        """
        D's greet method.
        Logic:
        - Starts the MRO chain
        - super().greet() calls B.greet (first parent in D(B, C))
        """
        print(f"Hello from D, {self.name}.")
        super().greet()  # Starts MRO chain (calls B.greet)

# Create an instance of D
d = D("Frank")

# Check MRO (Method Resolution Order)
print("MRO:", [cls.__name__ for cls in D.__mro__])
# Output: MRO: ['D', 'B', 'C', 'A', 'object']

d.greet()
# Execution flow follows MRO:
# 1. D.greet() executes -> prints "Hello from D, Frank."
# 2. super().greet() in D calls B.greet() (next in MRO)
# 3. B.greet() executes -> prints "Hello from B, Frank."
# 4. super().greet() in B calls C.greet() (next in MRO, NOT A!)
# 5. C.greet() executes -> prints "Hello from C, Frank."
# 6. super().greet() in C calls A.greet() (next in MRO)
# 7. A.greet() executes -> prints "Hello from A, Frank."
#
# Output:
# Hello from D, Frank.
# Hello from B, Frank.
# Hello from C, Frank.
# Hello from A, Frank.

# Key Point: A.greet() is only called ONCE despite being inherited by both B and C
# This is the solution to the diamond problem - Python's MRO ensures each class
# in the hierarchy is called exactly once, in a consistent order.

# ------------------------------------------------------------

# ============================================================================
# 5. HYBRID INHERITANCE (IMPROVED VERSION)
# ============================================================================
"""
Hybrid Inheritance: Combination of multiple inheritance types.
This example combines:
- Hierarchical inheritance (Animal -> Mammal and Animal -> Bird)
- Multiple inheritance (Bat inherits from both Mammal and Bird)

Structure:
         Animal
        /      \
    Mammal    Bird
        \      /
          Bat

IMPORTANT: Using super() for proper initialization chain.
"""

# Base class
class Animal:
    """
    Base class for all animals.
    Logic: Provides common attributes and methods for all animal types.
    """
    def __init__(self, name):
        """
        Base constructor for all animals.
        Logic: Initializes the name attribute for any animal.
        """
        self.name = name
        print(f"Animal.__init__ called for {name}")  # For demonstration

    def sound(self):
        """
        Generic sound method.
        Logic: Base behavior that all animals have.
        """
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical branch 1)
class Mammal(Animal):
    """
    Mammal class inheriting from Animal.
    Logic:
    - Represents mammals (warm-blooded, feed milk)
    - Part of hierarchical inheritance from Animal
    - Will be one parent of Bat (multiple inheritance)
    """
    def __init__(self, name):
        """
        Mammal constructor using super() for proper MRO.
        Logic: Calls parent's __init__ through super() chain.
        """
        super().__init__(name)  # Proper way to call parent constructor
        print(f"Mammal.__init__ called for {name}")  # For demonstration
    
    def feed(self):
        """
        Mammal-specific behavior.
        Logic: Mammals feed milk to their young.
        """
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Hierarchical branch 2)
class Bird(Animal):
    """
    Bird class inheriting from Animal.
    Logic:
    - Represents birds (can fly, have feathers)
    - Part of hierarchical inheritance from Animal
    - Will be another parent of Bat (multiple inheritance)
    """
    def __init__(self, name):
        """
        Bird constructor using super() for proper MRO.
        Logic: Calls parent's __init__ through super() chain.
        """
        super().__init__(name)  # Proper way to call parent constructor
        print(f"Bird.__init__ called for {name}")  # For demonstration
    
    def fly(self):
        """
        Bird-specific behavior.
        Logic: Birds can fly.
        """
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    """
    Bat class inheriting from both Mammal and Bird.
    Logic:
    - Demonstrates multiple inheritance (has characteristics of both)
    - Real bats are mammals that can fly (like birds)
    - MRO: Bat -> Mammal -> Bird -> Animal -> object
    - Using super() ensures proper initialization chain
    """
    def __init__(self, name):
        """
        IMPROVED: Using super() for proper MRO initialization.
        Logic:
        - super().__init__(name) follows MRO: Mammal -> Bird -> Animal
        - This ensures Animal.__init__ is called only ONCE
        - Avoids the diamond problem properly
        """
        super().__init__(name)  # Follows MRO: Mammal -> Bird -> Animal
        print(f"Bat.__init__ called for {name}")  # For demonstration

    def nocturnal(self):
        """
        Bat-specific behavior.
        Logic: Bats are active at night.
        """
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
print("Creating Bat instance:")
bat = Bat("Bruce")
print()  # Blank line for readability

# Initialization chain output:
# Animal.__init__ called for Bruce    <- Called once (proper MRO)
# Bird.__init__ called for Bruce      <- From MRO chain
# Mammal.__init__ called for Bruce    <- From MRO chain
# Bat.__init__ called for Bruce       <- Final initialization

# Check MRO
print("Bat MRO:", [cls.__name__ for cls in Bat.__mro__])
# Output: Bat MRO: ['Bat', 'Mammal', 'Bird', 'Animal', 'object']
print()

# Bat has access to methods from all parent classes
bat.sound()     # From Animal (2 levels up through both paths)
                # Output: Bruce makes a sound.
bat.feed()      # From Mammal
                # Output: Bruce is feeding milk.
bat.fly()       # From Bird
                # Output: Bruce is flying.
bat.nocturnal() # From Bat (own method)
                # Output: Bruce is nocturnal.

# ------------------------------------------------------------

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. SINGLE INHERITANCE: Child -> Parent (simple, linear)
   
2. MULTILEVEL INHERITANCE: Grandchild -> Parent -> Grandparent (chain)
   
3. HIERARCHICAL INHERITANCE: Multiple children from one parent (tree structure)
   
4. MULTIPLE INHERITANCE: Child inherits from multiple parents
   - Diamond Problem: When parents share common ancestor
   - Solution: Python's MRO (Method Resolution Order) with C3 Linearization
   - Always use super() to maintain proper chain
   
5. HYBRID INHERITANCE: Combination of multiple types
   - Most complex inheritance pattern
   - Requires careful MRO management
   - Use super() for proper initialization

BEST PRACTICES:
- Always use super() for calling parent methods (maintains MRO)
- Check MRO with ClassName.__mro__ when debugging
- Avoid deep inheritance hierarchies (prefer composition over inheritance)
- Document MRO expectations in complex multiple inheritance scenarios
"""