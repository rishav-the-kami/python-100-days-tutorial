import string
import random

code_or_decode = input("code or decode? ").lower()
sentence = input("Enter a sentence: ")
alphabets = list(string.ascii_lowercase)

def code():
    for word in sentence.split(" "):
        if len(word) >= 3:
            chars = [*word]
            chars.append(chars[0])
            chars.pop(0)
            
            for i in range(3):
                chars.insert(0, alphabets[random.randint(0, len(alphabets)-1)])
                chars.append(alphabets[random.randint(0, len(alphabets)-1)])

            word = "".join(chars)
        else:
            word = word[::-1]

        print(word, end=" ")
        

def decode():
    for word in sentence.split(" "):
        if len(word) < 3:
            word = word[::-1]
        else:
            word = word[3:-3]
            char = [*word]
            char.insert(0, char[len(char)-1])
            char.pop()
            word = "".join(char)
        
        print(word, end=" ")


if code_or_decode == "code": code()
else: decode()