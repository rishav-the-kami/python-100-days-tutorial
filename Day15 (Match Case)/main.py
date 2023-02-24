# Match Case - the switch case of javascript
x = int(input("Enter the value of x (from 1-3): "))

match x:
    # if x = 1
    case 1:
        print("x = 1")
    # if x = 2
    case 2:
        print("x = 2")
    # if x = 3
    case 3:
        print("x = 3")

    # the default of javascript
    case _ :
        print("kuch to sahi enter kar deta....")


# Using case with if-else (yup. imagine this feature in java. school would be sooooooo much easier ;-;)
y = int(input("enter y from 1-3: "))

match x:
    case 1 if y == 1:
        print("x = 1 and y = 1")
    case 1 if y == 2:
        print("x = 1 and y = 2")
    case 1 if y == 3:
        print("x = 1 and y = 3")

    # similarly do for x = 2 and x = 3 :D



# NOTE: u don needa add "break" after every case statement here unlike java. (FUCK I LOVE PYTHON ;-;)