# use the input function to prompt for user input
# now lets assign the name to a variable
# input is always of the string DT, so type cast if need tge input to be in integers
name = input("What is your name? ")
age = input("What is your age? ")
age = int(age)
age = age + 1
height = float(input("how tall are you? "))


print(("Hello ") + name)
print(("Your age is : ") + str(age))
print("Your height is : " + str(height) + "cm tall")
