# NOTE
# We cannot directly perform any operation on a tuple as its immutable. In order to do it, we convert the tuple to a list
# we perform wtv tf we wanna in the list and then convert the list back to the tuple
# Flowchart: Tuple -> List -> Some functions on the list.      Updated list -> Tuple
# Example:

countries_i_wanna_visit = ("Japan", "South Korea", "USA", "UK (again)", "Greece", "Phillippines")
temp = list(countries_i_wanna_visit)
temp.append("Germany")
temp.pop(countries_i_wanna_visit.index("Greece"))  # Removes Greece cuz it not that cool :/ Greece was boring..
countries_i_wanna_visit = tuple(temp)
print(countries_i_wanna_visit)


# NOTE we can concatenate 2 tuples without converting them to lists.
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = tuple1 + tuple2
print(tuple3)



# NOTE some important tuple functions (they work without converting the tuple to lists)
# count() - yk wat it does
# index() - again yk wat it does
# 
