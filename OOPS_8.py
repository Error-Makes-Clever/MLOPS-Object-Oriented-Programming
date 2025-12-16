# Method Overiding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Polymorphic behavior
animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()


# Method Overloading

class Shape:
    def area(self, length, width=None):
        """
        Calculate area
        - If only length: treat as square (length * length)
        - If length and width: treat as rectangle
        """
        if width is None:
            # Square: area = length^2
            return length * length
        else:
            # Rectangle: area = length * width
            return length * width

s = Shape()
print(s.area(5))       # Square: 25
print(s.area(5, 10))   # Rectangle: 50

