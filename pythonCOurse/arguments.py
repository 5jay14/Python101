# parameters and Arguments can be value, variable, collection
# or all sort of things. When a supply information to function. these are arguments when we supply arguments we need
# to supply matching number of parameters, these are parameters

# information passed when we call a function is called as arguments
# matching number of parameters will be set while defining the function

# positional arguments are those whose position matters
# ex


def positional_argument(fn, ln, age):
    print("Hello " + fn + ln)
    print("You are " + str(age) + " years old")


positional_argument("Vijay ", "Kumar", 21)


# keyword arguments
#  preceded by an identifier when we pass them to function. the order of the arguments does not
#  matter unlike positional arguments.

# ex

def keyword_arguments(fn, ln, age):
    print("hello " + fn + ln + " you are " + str(age) + " " + "years old")


keyword_arguments(ln="kumar", age=21, fn="vijay")
