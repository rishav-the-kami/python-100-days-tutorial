# Docstrings are the string literals that appear right after the definition of a function, method, class or module
# NOTE: Docstrings appear at the top of function body and other shits
# NOTE: docstrings != comments


def square(n):
    '''Takes in a number n, returns the square n'''
    print(n**2)


square(5)
print(square.__doc__)  # prints the docstring "Takes in a number n, returns the square n"
