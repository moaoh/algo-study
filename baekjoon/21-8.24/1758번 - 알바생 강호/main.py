t = int(input())
n = []
for x in range(t):
	n.append(int(input()))
n.sort(reverse=True)
tip = 0
for i, x in enumerate(n):
	x -= (i + 1 - 1)
	if x > 0:
		tip += x
print(tip)