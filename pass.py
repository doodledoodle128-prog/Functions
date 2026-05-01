for i in range (11):
    if i % 20 == 0:
        print("Fuzz")
    elif i % 15 == 0:
        pass
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("twist")
    else:
        print(i)