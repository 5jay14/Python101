# *args = Parameter that will pack all arguments into a tuple
#        Useful so that a function can accept varying amount of arguments, Tuples are ordered and unchangeable\
# in order to change the item in the tuple, cast it into list

def add (*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))