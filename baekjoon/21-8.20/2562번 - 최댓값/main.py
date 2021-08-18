n = []
for x in range(9):
	x = int(input())
	n.append(x)
print(max(n))
print(n.index(max(n)) + 1)