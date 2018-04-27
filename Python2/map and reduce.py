from functools import reduce
def str2float(s):
	def fn(x,y):
		return x*10+y
	n=s.index('.')
	s1=list(map(int,[x for x in s[:n]]))
	s2=list(map(int,[x for x in s[n+1:]]))
	return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)
print('\'123.4567\'=',str2float('123.4567'))