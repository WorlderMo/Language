L1=['adam','LISA','barT']
def normalize(name):
	return name.capitalize()  #return [L1[0].upper(),L1[1:].lower()]

L2=list(map(normalize,L1))
print(L2)