tup = (1, 2)
print(type(tup), tup)

tup = (1)
print(type(tup), tup)  # Surprisingly, the type is "int" and not "tuple"
# it is because python thinks that (1) is 1 in brackets. if u want the type to show as tuple with just one element then
tup = (1,)
print(type(tup), tup)


# NOTE tuple is immutable so tup[0] = <some value> will throw an error

if 2 in tup:
    print("2 is present in tuple")