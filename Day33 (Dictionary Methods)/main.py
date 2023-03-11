# SECTION update() - same as the update() in set methods
"""
Two managers, ep1 and ep2 have the performance of employees (out of 100). ep1 is at a higher position than ep2 so ep1 asks ep2
to give all its data in his sheet.
"""

ep1 = {1: 100, 2: 69, 3: 30}
ep2 = {4: 20, 5: 80, 6: 90}

ep1.update(ep2)
print(ep1)
print(ep2)


# SECTION clear() - empties the dictionary
ep2.clear()
print(ep2)


# SECTION pop(key) - removes the pair of the given key
pop_item = ep1.pop(2)
print(ep1)  # 2: 69 is removed
print(pop_item)  # VALUE of the key-value pair removed, i.e 69


# SECTION popitem() - removes the last element from the dictionary
ep1.popitem()
print(ep1)  # 6:90 is removed


# SECTION NOTE del (this time its important trust me)
# del ep1  # deletes the ep1 variable
del ep1[4]  # works the same as ep1.pop(4)
print(ep1)

# NOTE what if i enter some key which is not present in the dictionary using pop() or del?
# Answer: KeyError thrown.

# NOTE Now what if i use del ep1.get(key) instead of del ep1[key] (note that get() does not return any error, unlike [])
# del ep1.get(9)  # also shows an error


# SECTION Inserting a new element to the dictionary
ep1.update({69: "Yare yare"})
print(ep1)


# SECTION setdefault(key to look for, value to be added when the key is not present in the dictionary) - cant explain it so see the code ;-;
car = {
    "manufacturer": "Buggati",
    "model": "Bugatti Chiron"
}
print(car.setdefault("model", "Bugatti Veyron"))  # Output: Bugatti Chiron
# So what is the "Bugatti Veyron" doing here?
# Lets do it this way

print(car.setdefault("color", "What color's your bugatti?"))  # Output: What color's your bugatti?
print(car)  # note that it adds {"color": "What color's your bugatti?"} to the dictionary

"""so what it does is basically checks if the first argument (key) is in the dictionary or not
if its present, it will print the original value of the key. If its not present, then it will add a new key to the dictionary
with the value specified in the second argument"""



# SECTION dict.fromkeys(list/tuple of keys, value in all the keys) - creates a dictionary with the help of a list(or tuple) of keys and one value.
keys = ["Rishav", "AJ", "Jotaro"]  # u can also make it a tuple. doesnt matter
value = "Phenomenal"

dic = dict.fromkeys(keys, value)
print(dic)   # Output: {"Rishav": "Phenomenal", "AJ": "Phenomenal", "Jotaro": "Phenomenal"}

# NOTE what if i make a dictionary with only the keys and not the values. - all the keys will have None value
dic2 = dict.fromkeys(keys)
print(dic2)  # Output: {"Rishav": None, "AJ": None, "Jotaro": None}
