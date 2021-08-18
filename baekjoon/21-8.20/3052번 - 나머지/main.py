n = []
for x in range(10):
	x = int(input())
	x = x % 42
	if x not in n:
		n.append(x)
print(len(n))