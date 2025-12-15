from OOPS_3 import chatbook

# Using static method directly from class rather than obj

chatbook.set_id(1)

user1 = chatbook()
print(user1.id)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

# getter and setter

print(user1.get_name())
user1.set_name("Agent X")
print(user1.get_name())

print(user2.get_name())
user2.set_name("Agent Y")
print(user2.get_name())

print(user3.get_name())
user3.set_name("Agent X")
print(user3.get_name())


# Function vs Method 
lst = [1,2,3]

# function
a1 = len(lst)
print(a1)

# method
user1 = chatbook()
user1.sendmsg()