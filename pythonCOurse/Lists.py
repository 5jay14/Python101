# Used to store multiple items in a single variable. variable is now a list after using []
# each item in the list is referred to as an element


Food = ["Pizza", "Burger", "Sandwich", "Drinks"]
Food[0] = "Sushi"
# Food.append("Ice Cream") # adds an element at the end
# Food.remove("Drinks")
# Food.pop() # removes the last element
# Food.insert(0, "Cake")
# Food.sort() # sorts the list
# Food.clear() # Clears the list

print(Food)
print(Food[0])
print(Food[1])
print(Food[2])
print(Food[3])

for i in Food:
    print(i)
