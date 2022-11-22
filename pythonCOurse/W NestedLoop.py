# Nested loop = Loop inside the loop, it does not matter what loop it is.
# The inner loop will finish all of its iteration before finishing one iteration of the outer loop


rows = int(input("How many rows? : "))
columns = int(input("How many columns? : "))
symbol = input("Enter the symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")  #end prevents cursor from jumping to new line
    print() #print new line