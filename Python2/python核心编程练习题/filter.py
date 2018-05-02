def is_palindrome(s):
	return int(str(s))==int(str(s)[::-1])
output=filter(is_palindrome,range(1,1000))
print(list(output))