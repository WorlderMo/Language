from functools import reduce
def prod(x,y):
	return x*y

L=reduce(prod,[3,5,7,9])
print(L)