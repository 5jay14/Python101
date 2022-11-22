# Nested function calls = function calls inside other function calls, these are inner most function calls
# whichare resolved first, returned value is used as argument for the outer function

# num = input("enter a positive whole number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)


#nested function calls
print(round(abs(float(input("enter a positive whole number: ")))))