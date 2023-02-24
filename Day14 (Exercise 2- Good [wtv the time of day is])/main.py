import time

hour = time.localtime().tm_hour

print(time.strftime("%H:%M"))

if hour >= 0 and hour < 12:
    print("Good Morning")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon")
elif hour >= 17 and hour <= 19:
    print("Good Evening")
else:
    print("Good Night")


# NOTE
# %H - hour
# %M - minute
# %S - second
# %m - month
