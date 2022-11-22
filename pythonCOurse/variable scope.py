# local variable = available only in the region where it is created, ex - var defined inside the function
# Global variable = available globally inside or outside of any function

name = "vijayKumar"

def Disp_name():
    name = "vijay" # local scope (available only inside the function
    print(name)

Disp_name()
print(name)
# python follows the rule in the order L = local E = enclosing G= Global B = built in. Ex if we comment the local
# variable name defined in the function, the next available name is the global
