import math

a, b = map(int, input().split())

def lcm(a, b):
	return int(a * b / math.gcd(a, b))

print(math.gcd(a, b))
print(lcm(a, b))