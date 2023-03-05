# Suppose I am making a list of all my friends
# Some guy says Shubham. I add it.
# Now what if 1000 other guys say Shubham. I don wanna add 1000 shubham, i want only 1 unique name.
# This is where sets are used :D

a = {2, 4, 2, 6}
print(a)

# Expected Output: {2, 4, 2, 6}
# Real output: {2, 4, 6}  (the second 2 got ignored like how ur crush ignores u :) )

print(type(a))  # set

a = {}
print(type(a)) # dict


# To make an empty set
a = set()
print(type(a))  # set

a = {1, 2, 3, 4, 5}
# Accessing elements
for i in a:
    print(i)

print("Length of set:", len(a))
