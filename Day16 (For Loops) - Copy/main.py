# Printing all the letters of a string
my_name = "Rishav"

for letter in my_name:
    print(letter, end=" ")

print("\n")

# Printing all elements of a list
colors = ["Red", "Green", "Yellow", "Blue", "Orange"]

for color in colors:
    print(color)


# Printing the characters of every element of a list
for color in colors:
    print(color, "-", end=" ")
    for letter in color:
        print(letter, end=" ")

    print("")


# range(starting=0 (optional), end, step=1 (optional)) - range of loop
# Ex: range(5) - iterates from 0 to 4
# NOTE the first parameter, i.e. "starting" is optional. if not provided then it is taken as 0
# NOTE the last parameter, i.e. "step" is also optional. if not provided then it is taken as 1
for i in range(5):
    print(i)

print("\n")

# To print from 1 to 5 (not starting from 0)
for i in range(1, 5+1):
    print(i)

print("\n")

# Program to print even numbers upto 10
for i in range(2, 10+1, 2):
    print(i)

# So the last parameter that is "step" is the i++, i+=2, etc. (or Update Expression) of javascript.
