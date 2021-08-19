t = int(input())
for x in range(t):
	r, s = input().split()
	for y in s:
		print(y * int(r), end="")
	print()