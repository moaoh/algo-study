n = int(input())

if n < 100:
	print(n)
else:
	count = 99
	for x in range(100, n + 1):
		x = str(x)
		if int(x[0]) - int(x[1]) == int(x[1]) - int(x[-1]):
			count += 1
	print(count)