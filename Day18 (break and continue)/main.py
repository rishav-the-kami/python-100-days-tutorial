# Saral bhasha ma bole to:
# break: terminates the entire loop (rip loop ull not be missed)
# continue: skips 1 iteration (yup very understandable ikr)

# SECTION break
# In this program the loop is supposed to run 12 times, but it will terminate the moment 5 * i = 50
for i in range(13):
    print("5 x", i, "=", (5*i))

    # Now if (5*i) = 50, then the loop will terminate.
    if (5 * i) == 50: break

# Output: 5x1 to 5x10 (not till 5x12)


# SECTION continue
# *pata ha tujhe continue samajh ma nahi aaya*
# Program: Print all the even numbers
# NOTE Best way of coding:
"""
for i in range(2, 11, 2):
    print(i)
"""
# NOTE just to explain continue
for i in range(1, 11):
    if i % 2 == 0: print(i)
    else: continue

# here whenever i % 2 is not 0 that time the ongoing iteration terminates and the next iteration starts
# for ex: when i = 1, i % 2 is not 0 so the iteration terminates and moves on to the next value, i.e 2