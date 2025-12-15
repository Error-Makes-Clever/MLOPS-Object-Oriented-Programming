# Integer is class

my_int = 155
print(my_int)
print(type(my_int))

# String is class

my_str = "mlops playlist"
my_str = my_str.capitalize()
print(my_str)
print(type(my_str))

# List is class

lst = [1,2,3]
print(lst)
print(type(lst))

try:
    lst.capitalize()
except Exception as e:
    print(e)

# You can create your own datatype (Like Algebra Addition)

a = 'x'
b = 'y'
print(a+b)