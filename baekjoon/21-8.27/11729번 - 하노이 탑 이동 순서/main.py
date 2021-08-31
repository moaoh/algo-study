def top(n, start, end, middle):
	if n == 1:
		return print(start, middle)
	top(n - 1, start, middle, end)
	top(1, start, end, middle)
	top(n - 1, end, start, middle)

n = int(input())
print(2**n-1)
top(n, 1, 2, 3)