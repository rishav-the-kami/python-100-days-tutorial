# Suppose ur a beri smart programmer. ur coding smth which requests smth from a server.
# server fails to fulfil the request. in that case, usually an error occurs and the program terminates.
# now what if i want the program to not terminate when an error occurs. That time we use Exception Handling.
# Exception handling is represented by - Try, Except
# NOTE In short: Exception Handling is used to prevent the program from terminating when an error occurs

"""
TODO
a = int(input("Enter a number: "))
print(f'multiplication table of {a} is: ')

for i in range(1, 11):
    print(f"{a} X {i} = {a*i}")
"""

# It prints the multiplication table. cool.
# ab agar hamara user ek makkar, haraami, nihayati chutiya kisam ka aadmi nikla, aur usne koi String input kar diya.
# tab multiplication table calculate nahi ho payega. error create hoga aur program band.
# In these cases we use Try Except.


try:
    a = input("Enter a number: ")
    print(f'multiplication table of {a} is: ')

    for i in range(1, 11):
        print(f"{a} X {i} = {int(a)*i}")

except Exception as e:
    print("YOU THOUGHT THE PROGRAM WOULD END, BUT IT WAS ME, EXCEPTION!!!! KONO EXCEPTION DAA!!! *ok enough jojo reference*")
    print(e)

print("ha btw program didnt end :D L bozo")

# user ye dekhke mar jayega aur hame shanti milegi. happy ending :D


# NOTE btw btw, this type of error in the above code is called ValueError (cuz a string non-number cant be converted to int so its ValueError)
# so instead of except Exception as e or just except, i can be more specific and write - except ValueError: print("error msg")
# NOTE we can use multiple except.

# Example
try:
    arr = [1, 2, 3, 4]
    num = int(input("Enter index no.: "))
    print(f"No. {num+1} element of the array is {arr[num]}")

except ValueError:
    print("Enter integer value for the index")

except IndexError:
    print(f"There are only {len(arr)} elements in the array. {num} index not found.")

# In this program it prints "Enter integer value for the index" when the index entered is not convertable to integer.
# it prints "There are only...... index not found", when the index entered cannot be found in the array.
# NOTE IndexError occurs for index errors in the array.



# NOTE all the types of errors.
"""
AssertionError	Raised when the assert statement fails.
AttributeError	Raised on the attribute assignment or reference fails.
EOFError	Raised when the input() function hits the end-of-file condition.
FloatingPointError	Raised when a floating point operation fails.
GeneratorExit	Raised when a generator's close() method is called.
ImportError	Raised when the imported module is not found.
IndexError	Raised when the index of a sequence is out of range.
KeyError	Raised when a key is not found in a dictionary.
KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+c or delete).
MemoryError	Raised when an operation runs out of memory.
NameError	Raised when a variable is not found in the local or global scope.
NotImplementedError	Raised by abstract methods.
OSError	Raised when a system operation causes a system-related error.
OverflowError	Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	Raised when an error does not fall under any other category.
StopIteration	Raised by the next() function to indicate that there is no further item to be returned by the iterator.
SyntaxError	Raised by the parser when a syntax error is encountered.
IndentationError	Raised when there is an incorrect indentation.
TabError	Raised when the indentation consists of inconsistent tabs and spaces.
SystemError	Raised when the interpreter detects internal error.
SystemExit	Raised by the sys.exit() function.
TypeError	Raised when a function or operation is applied to an object of an incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translation.
ValueError	Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError	Raised when the second operand of a division or module operation is zero.
"""
