# ** kwargs = keyword arguments, packs all the arguments into dictionary

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


print(hello(title="Mr.", firstname="Vijay", LastName="Kumar"))
