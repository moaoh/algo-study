#! /usr/bin/python3

def	main():
	a, b, c = map(int, input().split())
	print("%d\n%d\n%d\n%d\n" %((a + b) % c, ((a % c) + (b % c)) % c, (a * b) % c, ((a % c) * (b % c)) % c), end = '')

if __name__ == '__main__':
	main()

