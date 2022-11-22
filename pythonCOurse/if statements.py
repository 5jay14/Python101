#  if statement = a block code that will be executed if the condition is true
# if we want to check more than one condition before reaching the else statement,
#  we can use else if statement, add that after else statement
#  else statement is executed as a last resort
# order of the statement matters

age = int(input("whats your age? = "))

if age == 100:
    print("You are a century old")
elif age >= 18:
    print("you are an adult")
elif age < 0:
    print("you haven't been born yet!! WTF")
else:
    print("You are a child!")
