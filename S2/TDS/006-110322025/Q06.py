l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39]

tuple_final = (tuple((x,y, x+y) for x in l1 for y in l2 if (x+y) % 2 == 0),tuple((x,y, x+y) for x in l1 for y in l2 if (x+y) % 2 != 0))

print(tuple_final)