import math

# SECTION Shit way
sentence = "Yoooo wsp my name is {} and I am {} years old"
name = "Rishav"
age = 15
print(sentence.format(name, age))  # places name and age in the respective {} brackets.

# this way of formatting requires adding the arguments in respective order. The alternate way is:
sentence = "Yooo wsp my name is {1} and I am {0} years old"
print(sentence.format(age, name))  # Same output as before.


# SECTION the better way (since format() sucks so we use f-strings cuz it better)
sentence = f"YOOOO mah name is {name} and I am {age} years old"
print(sentence)


# SECTION limiting the number of decimal places inside an fstring
pi_val = math.pi
print(f"The value of pi upto 3 decimal places is: {pi_val: .3f} and upto 4 decimal places is: {pi_val: .4f}")


# SECTION what if we wanna print the {name} literally (idw the name's value to be printed. i want to print "{name}")
print(f"We use {{name}} to print the name in an fstring")
