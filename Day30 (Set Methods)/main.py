# # SECTION union() - UNION IN SETS (value of variables dont change)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))

print(s1)
print(s2) 
# Both still remain the same


# SECTION update() - union of two sets but the value of the set changes
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.update(s2)
print(s1)


# SECTION intersection()
s1 = {1, 2, 3}
s2 = {3, 4, 5, 2}
print(s1.intersection(s2))
print(s1)

# SECTION interesection_update()
s1.intersection_update(s2)
print(s1)


# SECTION symmetric_difference(): union() - intersection() = symmetric_difference()
s1 = {1, 2, 3, 4, 5}
s2 = {4, 2, 0, 9, 8}
print(s1.symmetric_difference(s2))
# u get the point for symmetric_difference_update()


# SECTION difference() - prints the elements present ONLY in the original set
s1 = {"Japan", "Croatia", "France", "Germany"}
s2 = {"Germany", "Croatia", "Sweden", "India"}
print(s1.difference(s2))  # Output: France and Japan (as they are present only in the original set, i.e, s1)
# same for difference_update. u get the point


# SECTION isdisjoint() - returns True if 2 sets have no common elements.
# SECTION issuperset() - returns True if a set contains the elements of the other set
# SECTION issubset() - returns True if a set is a subset inside another set. For ex: {2, 3} is a subset in {1, 2, 3, 4} so it returns True


# SECTION add() - adds another element
s1 = {1, 2, 3}
s1.add(4)
print(s1)


# SECTION update() - adds more than one element. (alr seen above)

# SECTION remove() or discard() - removes an element (remove and discard both are same but just different names)
s1 = {"Japan", "Croatia", "India"}
s1.remove("Japan")
print(s1)

s1.add("Japan")

s1.discard("Japan")
print(s1)

# NOTE DIFFERENCE BETWEEN discard() and remove()
# discard() - does not raise an error if the given argument is not present in the set
# remove() - raises an error if the given argument is not present in the set


# SECTION pop() - removes the last element but we dk which elements get popped cuz sets are unordered.
s1 = {1, 2, 3, 4}
s1.pop()
print(s1)  # Expected: {1, 2, 3}
           # Reality: {2, 3, 4} (reason: we dk which element is where. sets are unordered. here 1 is the last element. somewhere else it may be idk but wtv u get the point dumb bitch)

# How to know wats the value which got popped?
s1 = {1, 2, 3, 4}
last_val_which_got_popped = s1.pop()
print(last_val_which_got_popped)


# SECTION NOTE del - not a function. it deletes a variable. like literally it just deletes a variable
del s1
# print(s1)  # throws an error

a = 2
del a
# print(a)  # throws an error
