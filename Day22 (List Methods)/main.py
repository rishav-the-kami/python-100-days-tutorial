l = [1, 2, 3, 4]
print(l)

# SECTION append() - adds an element to the end of the list
l.append(5)
print(l)


# SECTION sort()
l = [5, 2, 1, 3]
# Sorting in ascending order
l.sort()
print(l)
# Sorting in descending order
l.sort(reverse=True)
print(l)


# SECTION reverse() - reverses the list
l = [69, 420, 21]
print(l)
l.reverse()
print(l)


# SECTION index() - the indexOf() of javascript
print(l.index(420))  # Output: 1
# NOTE theres this important thing u needa know.
# index(value to be searched, starting index, end index).
# the last 2 parameters are not mandatory.
yo = [1, 2, 3, 4, 5, 4, 1, 3, 4, 6]
print(yo.index(4, 5, len(yo)))  # it slices 5:len(yo) and then searches for 4


# SECTION count() - checks how many times an element is occuring in a list
l = [1, 2, 3, 4, 1, 2, 1]
print(l.count(1))  # Output: 3


# SECTION copy()
l = [1, 2, 3, 4]
m = l
m[0] = 0
print(l)
# We are expecting [1, 2, 3, 4] but to our surprise it will be [0, 2, 3, 4].
# It is because m = l makes m have the same data address as l. so m and l are the same one list. we dont want that.
# we want m and l to be separate lists so we use copy() function

l = [1, 2, 3, 4]
m = l.copy()
m[0] = 0
print(l)  # now l is going to remain unaffected



# SECTION insert(index where u will insert the new element, element to be inserted)
l.insert(1, 89)
print(l)



# SECTION extend() - adds the list specified in the arguments to the target list
color = ["Violet", "Indigo", "Blue", "Green"]
color2 = ["Yellow", "Orange", "Red"]
print(color)
color.extend(color2)
print(color)



# SECTION concatenating 2 lists
l1 = ["Yare Yare Daze"]
l2 = ["Muda Muda"]

k = l1 + l2
print(k)


# NOTE Difference between extend() and concatenation
# extend changes the value of the list itself. Here color.extend(color2) added color2 to color. so value of color changed
# concatenation just concats two lists in a new variable. the original lists remain unaffected



# SECTION pop(index) - removes the element in the specified index