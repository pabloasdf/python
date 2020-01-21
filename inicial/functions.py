def hello(name="pablo"):
    print("HellO " + name)

hello("joe")
hello()

def add(numberOne, numberTwo):
    return numberOne + numberTwo
    
print(add(10, 30))

add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10, 30))