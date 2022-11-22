import time

# For loop = A statement that executes its block of code a limited amount of times
# Benefit of for loop is that, we can iterate through anything that is iterable, string or collections
# range is a function

for i in range(10):
    print(i)

for v in range(0, 50):  # First number is inclusive and 2nd is exclusive
    print(v)

# We can add Third argument in the range function, this functions as step, how much we want to count up or down by
for k in range(0, 100, 2):
    print(k)

for j in "vijay kumar":
    print(j)  # prints each letter in seperate line

for seconds in range(10, 0, -1):
    time.sleep(1)
    print(seconds)

print("Happy new year")
