def cube(num):
    return num*num*num
print(cube(3))

def cube (num):
    return num*num*num
result = cube(4)
print(result)

def add (a,b):
    print(f"ADDING {a} + {b}")
    return a+b
def subtract (a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b
def multiply (a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b
def divide (a,b):
    print(f"DIVIDING {a}/{b}")
    return a/b
age = add(10, 8)
height = subtract(20, 5)
weight = multiply(10, 5)
iq = divide(100, 2)
print(f"AGE: {age}, HEIGHT: {height}, WEIGHT: {weight}, IQ: {iq}")

# A puzzle for extra credit, type it in anyway
print("HERE IS A PUZZLE")
what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print(f"That becomes {what} Can you do it by hand?")
