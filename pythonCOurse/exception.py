# Exception = Events detected during execution that interrupt the flow of a program
# it is a good practise to catch specific exceptions first and end the catch block with general exception
# Finally block will always execute does not matter what occurs

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter only number Please")
except Exception:
    print("something went wrong :(")
finally:
    print("THis will always execute")