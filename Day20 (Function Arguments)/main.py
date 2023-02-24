def average(a, b):
    print("The average is:", (a+b)/2)

average(4, 6)

# Giving default values
def mean(a=30, b=20):
    print("The mean is:", (a+b)/2)

mean(50)  # changes the value of a from 30 to 50 but b remains 20
mean(b=30) # changes the value of b from 20 to 30 but a remains 30


# Setting value of arguments in any order
average(b=5, a=10)


# Passing infinite arguments
# num is a tuple
def yareyare(*num):
    sum = 0
    for i in num:
        sum += i
    print("Average is:", sum/len(num))


yareyare(1,2,3,4,5,6,7,8,9,10,11,12,13)


# Passing arguments in the form of dictionary
def smth(**lol):
    print(lol["fname"], lol["lname"], "u are", lol["age"], "years old")

smth(fname="Rishav", lname="Sarkar", age="15")
