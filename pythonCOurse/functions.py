# block of code executed only when it is called Arguments and parameters Arguments can be value, variable, collection
# or all sort of things. When a supply information to function. these are arguments when we supply arguments we need
# to supply matching number of parameters, these are parameters

# information passed when we call a function is called as arguments
# matching number of parameters will be set while defining the function
import time


def count():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("happy new year")


# count()

# Ex 1 = supplying value. name and age is temp variable
def hello(name, age):
    print("hello " + name)
    print("you are " + str(age) + " years old")

hello("vijay", 28)

# Ex 2, supplying variable

my_name = "kumar"
hello(my_name, 21)