a = "yare yare daze"
b = "bROOO"
print(a.upper())
print(b.lower())

# rstrip() - removes the railing characters
c = "hootiyapa band karo jajajajajajajajaja"
print(c.rstrip("ja"))  # removes all the "?"


# replace() - khud samajh ja gavar
d = "Rishav is shit"
print(d.replace("shit", "Phenomenal!"))


# split() - yk arrays right (nahi pata to doob ke marja)? ha to the characters of a specified group are one array
e = "There are 4 words"
# printing no. of WORDS (not characters) in the string
print(len(e.split(" ")))


# ok heres a challenge.... convert the first letter to capital and not the rest
f = "kuch maal"
f = f[0].upper() + f[1:]
print(f)

# *thats how mf like u code :D* 
# le iska simple version
print(f.capitalize())

# capitalize() - make the first letter upper case, the rest are as it is.
# also look at this :D
g = "hEllO"  # ha pata ha ganja phook ke likha hu hello
print(g.capitalize())  # Output: Hello (ha sabka uppercase, lowercase sudhar diya...)


# center() - khud dekhle kya karta ha, itna explain nahi kar raha ha baithke 🗿
print(e.center(50))
print(len(e))  # 17
print(len(e.center(50)))  # 50 (so it adds 33 (50-17 = 33) spaces to center it)


# count() - to see how many times a given string is repeated inside another string
h = "LOL LOL LOL LMAO"
print(h.count("LOL"))  # output: 3


# startswith() and endswith() - yk it from java
# now heres smth nice :D
i = "LMFAO BRO"
print(i.endswith("B", 4, 7))
# here it checks if the string starting from index 4 to end index 7-1 (6), ends with "B" or not


# find() - indexOf() of javascript
j = "Kisenai ima mo, tomarenai ima mo"
print(j.find("ima mo"))  # Output: 8

# index() - its a lot similar to find() but find() returns -1 when no occurence is found whereas index() throws an error


# isalnum() - checks whether a string is alphanumeric or not
j = "!@fefg$@$@dxhgebg"
print(j.isalnum())  # False
j = "myRogueArc"
print(j.isalnum())  # True

# isalpha() - checks whether a string contains only strings or a combination of strings numbers special chars blah blah blah
print(j.isalpha())  # True
j = "1234yeeee"
print(j.isalpha())  # False


# islower() - returns true if all characters are lower case


# isprintable() - returns false if a string contains a non graphic character (like \n)


# istitle() - returns true if the first letter of each words are capitalized
j = "happy valentines day"  # yea im single.... and im typing this shit on 13th feb 10:38 p.m.....
print(j.istitle())  # False
j = "Happy Valentines Day"
print(j.istitle())  # True

# title() - capitalises the first letter of each word
j = "the cold within"
print(j.title())  # Output: The Cold Within

# swapcase() - lower case ko uppercase aur uppercase ko lower case
j = "PRiTam ChaNdra"
print(j.swapcase())  # Output: prItAM cHAnDRA