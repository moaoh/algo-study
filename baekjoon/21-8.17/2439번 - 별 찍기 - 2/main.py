n = int(input())

for x in range(n):
	print(" " * (n - (x+1)), end="")
	print("*" * (x+1))