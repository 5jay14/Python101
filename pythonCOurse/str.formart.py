# str.format =  Optional method that gives users more control when displaying output
# can use variables or values as an option, position oriented

animal = "cow"
place = "moon"


#print("the {} jumped over the {}".format(animal,place))
#print("the {} jumped over the {}".format("cow","moon"))

#positional arguments
#print("the {1} jumped over the {0}".format(animal,place))

#kw arguments, here the external variables are not required, because they are defined inside the format
#print("the {animal} jumped over the {place}".format(animal="cow", place="moon"))
#print("the {animal} jumped over the {animal}".format(animal="cow", place="moon"))


text = "the {} jumped over the {}"
print(text.format(animal,place))

#padding to the strings, use collan inside the {}
name = "bro"
print("hello, my name is {:10} nice to meet you".format(name))
print("hello, my name is {:<10} nice to meet you".format(name))
print("hello, my name is {:>10} nice to meet you".format(name))
print("hello, my name is {:^10} nice to meet you".format(name))


#formatting number using the format method

number = 3.14159
number1 = 1000
print("the number pi is {:.2f}".format(number)), #this will output only 2 decimals. f = floating point number(decimal portion
print("the number pi is {:.3f}".format(number))
print("the number is {:,}".format(number1))
print("the number is {:b}".format(number1)) #binary
print("the number is {:X}".format(number1)) #hexa decimal, lower/upper case X
print("the number is {:o}".format(number1))  #octo
print("the number is {:E}".format(number))  #scientific notation