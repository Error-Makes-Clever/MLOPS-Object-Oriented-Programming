# ============================================================================
# DIAMOND INHERITANCE: COMPARING SUPER() CHAIN BEHAVIOR
# ============================================================================
"""
This file demonstrates three different scenarios of super() usage in 
diamond inheritance to show how the MRO (Method Resolution Order) chain works.

Diamond Structure:
        A
       / \
      B   C
       \ /
        D

MRO for D: D → B → C → A → object
"""

# ============================================================================
# CODE 1: C DOES NOT CALL SUPER() - CHAIN BREAKS AT C
# ============================================================================
print("="*70)
print("CODE 1: C does NOT call super() - Chain breaks at C")
print("="*70)

class A1:
    """Base class - Top of the diamond"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}.")

class B1(A1):
    """Left branch of diamond - Calls super()"""
    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()  # ✓ Continues chain to next in MRO (C)

class C1(A1):
    """Right branch of diamond - Does NOT call super()"""
    def greet(self):
        print(f"Hello from C, {self.name}.")
        # super().greet()  # ✗ COMMENTED OUT - Chain STOPS here!
        # Even though A is next in MRO, it will never be called

class D1(B1, C1):
    """Bottom of diamond - Inherits from both B and C"""
    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet()  # Starts the chain (calls B.greet)

# Execute Code 1
d1 = D1("Frank")
print("\nMRO:", [cls.__name__ for cls in D1.__mro__])
print("\nCalling d1.greet():")
d1.greet()

print("\n--- Analysis of Code 1 ---")
print("Execution Flow:")
print("1. D.greet() executes → prints 'Hello from D' → calls super()")
print("2. B.greet() executes → prints 'Hello from B' → calls super()")
print("3. C.greet() executes → prints 'Hello from C' → NO super() call")
print("4. A.greet() NEVER executes ✗ (chain broken at C)")
print("\nResult: Only D, B, C print. A is skipped!")
print("="*70)

# ============================================================================
# CODE 2: BOTH B AND C CALL SUPER() - COMPLETE CHAIN (CORRECT)
# ============================================================================
print("\n" + "="*70)
print("CODE 2: Both B and C call super() - Complete chain ✓")
print("="*70)

class A2:
    """Base class - Top of the diamond"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}.")

class B2(A2):
    """Left branch of diamond - Calls super()"""
    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()  # ✓ Continues chain to next in MRO (C)

class C2(A2):
    """Right branch of diamond - Calls super()"""
    def greet(self):
        print(f"Hello from C, {self.name}.")
        super().greet()  # ✓ Continues chain to next in MRO (A)

class D2(B2, C2):
    """Bottom of diamond - Inherits from both B and C"""
    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet()  # Starts the chain (calls B.greet)

# Execute Code 2
d2 = D2("Frank")
print("\nMRO:", [cls.__name__ for cls in D2.__mro__])
print("\nCalling d2.greet():")
d2.greet()

print("\n--- Analysis of Code 2 ---")
print("Execution Flow:")
print("1. D.greet() executes → prints 'Hello from D' → calls super()")
print("2. B.greet() executes → prints 'Hello from B' → calls super()")
print("3. C.greet() executes → prints 'Hello from C' → calls super()")
print("4. A.greet() executes → prints 'Hello from A' ✓ (chain complete)")
print("\nResult: All classes execute! This is the CORRECT implementation.")
print("="*70)

# ============================================================================
# CODE 3: NEITHER B NOR C CALL SUPER() - CHAIN BREAKS AT B
# ============================================================================
print("\n" + "="*70)
print("CODE 3: Neither B nor C call super() - Chain breaks at B")
print("="*70)

class A3:
    """Base class - Top of the diamond"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}.")

class B3(A3):
    """Left branch of diamond - Does NOT call super()"""
    def greet(self):
        print(f"Hello from B, {self.name}.")
        # super().greet()  # ✗ COMMENTED OUT - Chain STOPS here!

class C3(A3):
    """Right branch of diamond - Does NOT call super()"""
    def greet(self):
        print(f"Hello from C, {self.name}.")
        # super().greet()  # ✗ COMMENTED OUT (won't be reached anyway)

class D3(B3, C3):
    """Bottom of diamond - Inherits from both B and C"""
    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet()  # Starts the chain (calls B.greet)

# Execute Code 3
d3 = D3("Frank")
print("\nMRO:", [cls.__name__ for cls in D3.__mro__])
print("\nCalling d3.greet():")
d3.greet()

print("\n--- Analysis of Code 3 ---")
print("Execution Flow:")
print("1. D.greet() executes → prints 'Hello from D' → calls super()")
print("2. B.greet() executes → prints 'Hello from B' → NO super() call")
print("3. C.greet() NEVER executes ✗ (chain broken at B)")
print("4. A.greet() NEVER executes ✗ (chain broken at B)")
print("\nResult: Only D and B print. Both C and A are skipped!")
print("="*70)

# ============================================================================
# SIDE-BY-SIDE COMPARISON SUMMARY
# ============================================================================
print("\n" + "="*70)
print("SIDE-BY-SIDE COMPARISON")
print("="*70)

comparison_table = """
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   Class     │   CODE 1    │   CODE 2    │   CODE 3    │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ D calls     │     ✓       │     ✓       │     ✓       │
│ super()?    │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ B calls     │     ✓       │     ✓       │     ✗       │
│ super()?    │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ C calls     │     ✗       │     ✓       │     ✗       │
│ super()?    │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ A executes? │     ✗       │     ✓       │     ✗       │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ Output      │ D, B, C     │ D, B, C, A  │ D, B        │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ Chain       │ Broken at C │ Complete ✓  │ Broken at B │
│ Status      │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
"""
print(comparison_table)

# ============================================================================
# VISUAL REPRESENTATION OF MRO CHAIN EXECUTION
# ============================================================================
print("\n" + "="*70)
print("VISUAL REPRESENTATION OF MRO CHAIN")
print("="*70)

print("""
MRO for all: D → B → C → A

CODE 1 (C breaks chain):
    D ✓ → B ✓ → C ✓ → A ✗
                  ↑
            Chain breaks here
            (C doesn't call super)

CODE 2 (Complete chain - CORRECT):
    D ✓ → B ✓ → C ✓ → A ✓
                          ↑
                    All execute!
                    (Everyone calls super)

CODE 3 (B breaks chain):
    D ✓ → B ✓ → C ✗ → A ✗
             ↑
        Chain breaks here
        (B doesn't call super)
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
print("="*70)
print("KEY TAKEAWAYS")
print("="*70)

takeaways = """
1. COOPERATIVE SUPER():
   - For the full MRO chain to execute, EVERY class must call super()
   - It's called "cooperative" because all classes must cooperate

2. BREAKING THE CHAIN:
   - If ANY class doesn't call super(), the chain stops there
   - All classes after it in the MRO won't execute

3. CORRECT IMPLEMENTATION:
   - Code 2 is the ONLY correct implementation
   - In multiple inheritance, all intermediate classes should call super()

4. DIAMOND PROBLEM SOLUTION:
   - super() ensures base class (A) is called only ONCE
   - Without super(), A could be called multiple times through different paths

5. BEST PRACTICE:
   ✓ GOOD:
   def method(self):
       # Do your work
       super().method()  # Always call super()
   
   ✗ BAD:
   def method(self):
       # Do your work
       # No super() call - breaks the chain!

6. EXCEPTION:
   - Only the final base class (like A) should NOT call super()
   - Because there's nothing after it in the MRO
"""
print(takeaways)
print("="*70)

# ============================================================================
# PRACTICAL EXAMPLE: WHY THIS MATTERS
# ============================================================================
print("\n" + "="*70)
print("PRACTICAL EXAMPLE: Why This Matters")
print("="*70)

print("""
Imagine a real-world scenario with mixins:

class DatabaseMixin:
    def save(self):
        print("Saving to database...")
        super().save()  # ← Must call super()!

class CacheMixin:
    def save(self):
        print("Updating cache...")
        super().save()  # ← Must call super()!

class Model:
    def save(self):
        print("Validating data...")

class User(DatabaseMixin, CacheMixin, Model):
    def save(self):
        print("Saving user...")
        super().save()

# If any mixin forgets super().save(), the chain breaks!
# You might save to database but forget to update cache (or vice versa)
# This causes bugs that are hard to track down.
""")

print("="*70)
print("END OF COMPARISON")
print("="*70)