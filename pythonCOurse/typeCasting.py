# convert the datatype of a value to another data type
# when is it needed? scroll down

x = 1
y = 2.0
z = "3"

# type casting
int(y)
print(x)


# one more way
print(int(z))

# permanent change
y = int(y)
print(y)

# when is it needed?
# since we cannot normally concatenate string or float with integer.
# But we need to combine above variables with another data type

# This is when we need type casting

# example
a = 1
b = 2.95
c = "3"

print("Value of A is" " " + str(a))
print("Value of B is" " " + str(b))
