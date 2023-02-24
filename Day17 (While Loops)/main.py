# Printing from 1 to n
n = int(input("Enter n: "))

i = 1
while i <= n:
    print(i, end=" ")
    i += 1

print("\n")


# Printing n to 1
n = int(input("Enter n: "))

while n >= 1:
    print(n, end=" ")
    n -= 1

print("\n")


# Take input of something unless its 69 and tell how many it times took to input 69
i = int(input("Enter number: "))
c = 1

while i != 69:
    i = int(input("Enter number: "))
    c += 1

if c == 69 or c == 420 or c == 21:
    print("nice")
elif c == 96:
    print("dukh hua ;-;")
elif c == 1:
    print("Pahli baar ma maan gaya launda :smirk:")
else:
    print("it took u", c, "times to enter 69")


# NOTE you can use else statement with while loop (yup..)
# The else block is executed as soon as the program comes out of the while loop. (ab agar tum kutto ki tarah infinite loop chalaoge tab to is janam ma nahi run karega else wala block)
# For example

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("I am inside else :D")

# Output:
# 1
# 2
# 3 
# 4 
# 5
# I am inside else :D



# NOTE python doesnt have do while loop... sadly
# Emulating do while loop in python!

i = int(input("Enter a number: "))

if i > 5:
    print("lol (but pretend its the \"do\" part)")
while i <= 5:
    print("lol")

