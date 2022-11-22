#  While loop = A stetement that executes the block of code as long as the condition remains true
#  Runs unlimited time

# While loop = unlimited execution
# For loop = Limited execution (Since we already define in the statement itself)

name = ""

while len(name) == 0:
    name = input("Enter your name: ")
    print("Hello "+name)