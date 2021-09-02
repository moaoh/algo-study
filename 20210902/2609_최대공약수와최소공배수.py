#! /usr/bin/python3

def	get_gcd(a:int, b:int):
	n = a % b
	if n == 0:
		return b
	return get_gcd(b , n)

def	main():
	a, b = map(int, input().split())
	gcd = get_gcd(a, b)
	lcm = a * b // gcd
	print(gcd, lcm, sep = '\n')

if __name__ == '__main__':
	main()
