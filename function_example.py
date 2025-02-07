def greet():
    """
    Simple function printing hello
    :return:0
    """
    print("hello")
    return 0

greet()
x= greet()
print(x)

def greet_improved(name):
    """
    More complex greet that takes a name as a param
    :param name: name of person to greet
    :return: None
    """
    print("hello",name)
greet_improved("John")
greet_improved("Jane")

def custom_op(x=0,y=0):
    """
    Custom op: 10x+y
    :param x: first number
    :param y: second number
    :return: number, 10x+y
    """
    result=10*x+y
    return result
print(custom_op(5,8))
x=custom_op(5,9)
print(f"the result of custom_op is:{x}")
print(custom_op(5,9))
x=custom_op(y=9,x=5) #arguments by name
print(f"result of custom_op is:{x}")
print(custom_op(5))
print(custom_op())
print(custom_op(y=9))

def bond_intro(name):
    print("the name is:", name)

def bond_name(first="James", last="Bond"):
    return f"{last}, {first} {last}"
print(bond_name("Marina", "García"))
bond_intro(bond_name("Marina", "García"))
bond_intro(bond_name())
