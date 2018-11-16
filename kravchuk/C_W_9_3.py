a = (('1', 1),('2', 2),('3', 3))
my_dict = {b[0]: c for b in a for c in b}

print(my_dict)