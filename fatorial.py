def factor(x):
    '''this is a resursion function'''
    if x == 1 or x == 0:
        return 1
    else:
        return x*factor(x-1)
    
print("the factor of 0:", factor(0))
print("the factor of 1:",factor(1))
print("the factor of 2:",factor(2))
print("the factor of 5:",factor(5))
print("the factor of 10:",factor(10))
