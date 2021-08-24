def sum(s):
	n = 0
	for x in s:
		n += int(x)
	return n
a, b = input().split()
a = sum(a)
b = sum(b)
print(a * b)