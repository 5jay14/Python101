# sets = collection which is unordered and un-indexed. No duplicate values

dishes = {"bowl", "cup", "plate", "knife"}
utensils = {"spoon", "knife", "fork"}

dishes.add("tumbler")  # adds an element
dishes.remove("bowl")  # removes an element
print(dishes.difference(utensils)) #  this prints what dishes have that utensils doesn't
print(dishes.intersection(utensils)) #  returns which is common in both sets
#  dishes.update(utensils) # combines elements of two sets
# dishes.clear()



dinnerTable = dishes.union(utensils) #  combines multiple sets to form new one
for y in dinnerTable:
    print(y)

