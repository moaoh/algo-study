import sys

t = int(sys.stdin.readline().rstrip())

for n in range(int(t)):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	print(a + b)