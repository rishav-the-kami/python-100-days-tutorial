# Dictionaries are objects in javascript

# Suppose im creating a real dictionary
dic = {
    "Phenomenal": "Marvelous",
    "UwU": "A term used by furries",
    "Sweety": "A term used by Kami~",
    "Peanuts": "very important food material for anya",
    "Stoopid": "ask snow the meaning :skull:"
}

word = (input("Which word do u want meaning for: ")).title()

print(f'{word}: {dic[word]}')



# Storing names of ppl acc to their employee id
dic2 = {
    69: "Rishav",
    420: "Kami~",
    21: "Also Rishav :)",
    96: "Not Rishav this time ;-;"
}

employee_id = int(input("Enter employee id: "))
print(f'{employee_id} is {dic2[employee_id]}')


"""
NOTE now theres a problem. Suppose i enter a word or an employee id which is not present in the dictionary.
it will show me an error. To not get errors we use .get() instead of []
Incase no key is found in the dictionary, the output is None
"""

print(dic2.get(72))  # Output: None (no errors)
print(dic2.get(69))  # Output: Rishav


# SECTION to get all the keys. we use keys() method in the dictionary. it returns a List (or array) of keys.
for keys in dic2.keys():
    print(keys, end="")

print()

# SECTION to get all values: values(). stored in list format
for values in dic2.values():
    print(values, end="")

print()

# SECTION accessing key-value pairs - items()
print(dic.items())

for key, value in dic.items():
    print(f'{key}: {value}')
