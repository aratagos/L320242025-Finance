from functools import reduce

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def ajoute(a, b):
    return a + b

integers = map(int, numbers)

total = reduce(ajoute, integers)

print(total)

