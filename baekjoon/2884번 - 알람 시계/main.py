h, m = map(int, input().split())

only_m = h * 60 + m - 45

if only_m < 0:
	only_m += 24 * 60
print(only_m // 60, only_m % 60)