#  Logical operators = and, or ,not, used to check two or more statements.
# and = all the condition must be true for the statement to be executed
# or = statement will be executed even if any 1 of the condition is true
# not = it reverses, if the statement is true, it turns into false. vise versa

temp = int(input("whats the temperature outside?"))

if temp >= 0 and temp <= 30:
    print(" its a good day, go out")
elif temp <= 0 or temp >= 30:
    print("Its still a good day, go out")

#not

if not(temp >= 0 and temp <= 30):
    print(" its a good day, go out")
elif not(temp <= 0 or temp >= 30):
    print("Its still a good day, go out")
