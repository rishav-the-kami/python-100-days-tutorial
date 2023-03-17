marks = [12, 56, 38, 98, 69]

# What if i wanna print "NOICE {marks}" when the 3rd index element comes in a loop?
# dumb u gonna code like this
for i in range(len(marks)):
    if i == 3:
        print(f"NOICE {marks[i]}")

wee = enumerate(marks)

# better way to code this
for index, marks in wee:
    if index == 3:
        print(f"NOICE {marks}")


# by default enumerate starts from 0, which we know. but we can specify our own starting index.
# for index1, marks1 in enumerate(marks, start=1):
#     if index1 == 3:
#         print(f"NOICE {marks}")

# Output: NOICE 38
