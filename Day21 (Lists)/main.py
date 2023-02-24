# List = Array. Ha thats it
marks = [10, 8, 7]
print(marks)
print(type(marks))  # <class 'list'>

# yk how to access individual elements.
marks[0] # first element
marks[1] # second element
marks[2] # third element

# NOTE: LISTS ARE MUTABLE AND TUPLES ARE IMMUTABLE (dont ask me what tuple is. idk myself rn)

# can we add values of other datatypes in a list? ans: yup
markslmao = [10, 20, 30,40, "RISHAVVVV"]  # does **NOT** throw an error


# Guess output of this:
print(marks[-2])  # Output: 8.... Reason: Just like strings, lists also sees marks[-2] as marks[len(marks)-2] = marks[3-2] = marks[1] = 8

# Checking if an element exists in a list or not
if 10 in marks:
    print("someone got full marks")
else:
    print("no one got full marks")

# Same can be done for a string
name = "Rishav"

if "Rish" in name:
    print("Rish exists")
else:
    print("Rish does not exist")


# Printing all the elements (in the form of a list. not individually)
# two ways
# 1
print(marks)

#2
print(marks[:])


# NOTE List slicing is the exact same as string slicing. EXACT SAME.

# NOTE additional feature: jump index
shit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(shit)
print(shit[1:5])  # [2, 3, 4, 5]
print(shit[1:5:2]) # the last value "2" denotes the skipping while slicing. Output: [2, 4] (3 and 5 are skipped)
print(shit[1:5:3]) # Output: [2, 5]



# Creating a list on the spot
words = ["UWU", "OWO", "<3", "I miss discord ;-;", "Yare yare daze", "idk if u can see it or not. but. SHUNIKA :D", "OOof"]
names_starting_with_o = [word for word in words if word[0].upper() == "O"]
print(names_starting_with_o)
