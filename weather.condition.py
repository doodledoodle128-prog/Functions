def weather(spring, autumn):
    print("The weather is good in:", spring)
    print("The weather is the same in:", autumn)
    return spring, autumn

spring = "autumn"
autumn = spring
weather(spring, autumn)