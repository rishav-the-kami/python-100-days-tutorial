# String slicing and Operations in strings

#TODO Normal slicing
names = "Rishav, Kiyochi, Kami, HELIO, D.I."
# Printing Rishav only (fuck the other names)
print(names[0:6])  # You can also write names[:6] (omit the 0, no one gaf)

# NOTE
# R I S H A V
# 0 1 2 3 4 5
# but i wrote 0:6 (6 not 5)     hence while string slicing, startIndex = normal python index and endIndex = our counting (i.e start counting from 1 and not 0)
print(names[0:0])  # Output: A FUCKING BLANK SPACE

#TODO Negative slicing
fruit = "Fruit"
print(fruit[0:-3])  # Output: Fr
# How does it work?
# fruit[0:-3] is equivalent to fruit[0:len(fruit)-3] = fruit[0:5-3] = fruit[0:2] hence its Fr

print(fruit[-3:-1])  # Output: ui
# How does it work?
# fruit[-3:-1] = fruit[len(fruit)-3:len(fruit)-1] = fruit[5-3:5-1] = fruit[2:4] = ui

# Finding length of a string
someString = "BRO"
print(len(someString))  # Output: 3 (very obvious ik)
