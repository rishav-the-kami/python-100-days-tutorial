# Strings

a = "Basic String with double quotes"
b = 'Basic string with single quotes'

c = 'Rohan said "Wassup"'
d = "Rohan said \"Wassup\""

e = "Yooo\nok next line\nanother line"
f = """Yooo
ok next line
another line"""  # u can also use ''' ''' instead of """ """

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# Printing first letter
print(a[0])  # the .charAt(int index) function in java where index starts from 0
print(a[1])
print(a[2])

# Printing individual letters of a string
for character in c:
    print(character)
