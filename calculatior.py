def add(P, Q):
    return P + Q\

def sub(P, Q):
    return P - Q

def div(P, Q):
    return P / Q

def multi(P, Q):
    return P * Q

while True:
    print("Choose between:")
    print("a: addition")
    print("b: subtration")
    print("c: Division")
    print("d: Multiplication")
    choice = input("choose betwwn a,b,c,d: ")

    num1 = int(input("What is your first number?: "))
    num2 = int(input("what is your second digit?: "))

    if choice == "a":
        print(num1, "+", num2, "=", add(num1,num2))
    if choice == "b":
        print(num1, "-", num2, "=", sub(num1,num2))
    if choice == "c":
        print(num1, "/", num2, "=", div(num1,num2))
    if choice == "d":
        print(num1, "x", num2, "=", multi(num1,num2))
