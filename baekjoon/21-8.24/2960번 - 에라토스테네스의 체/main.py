n, k = map(int, input().split())
e_list = list(range(n + 1))

def eratos():
	count = 0
	for x in range(2, n + 1):
		if e_list[x] != 0:
			for y in range(x, n + 1, x):
				if e_list[y] != 0:
					e_list[y] = 0
					count += 1
					if count == k:
						return y
print(eratos())