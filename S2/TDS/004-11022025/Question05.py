dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"g": 7, "h": 8, "i": 9}

def change_dict(d1, d2):
    dictemp= {}
    for d1key, d2value in zip(d1.keys(), d2.values()):
        dictemp[d1key] = d2value
    return dictemp

dict3 = change_dict(dict1, dict2)

print(f'dict1: {dict1}')
print(f'dict2: {dict2}')
print(f'dict3: {dict3}')