a = [1, 4, 2, 5, 3, 2]
b = [1, 3, 42, 5, 2, 3, 2]
c = [a.count(i) == b.count(i) for i in set(a)]
print(c)
