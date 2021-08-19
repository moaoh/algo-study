a = [-1] * 26
s = input()
for x in s:
	a[ord(x) - ord('a')] = s.find(x)
for x in a:
	print(x, end=" ")