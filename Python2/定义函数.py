import math

def quadratic(a,b,c):
	temp=b*b-4*a*c
	if temp>=0:
		x1=(-b+math.sqrt(temp))/(2*a)
		x2=(-b-math.sqrt(temp))/(2*a)
		return x1,x2
	else:
		return '无解'
r=quadratic(2,3,1)
print(r)
