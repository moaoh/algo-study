#! /usr/bin/python3

def	main():
	a, b = map(int, input().split())
	print("%d\n%d\n%d\n%d\n%d\n" %(a + b, a - b, a * b, a / b, a % b), end = '')

if __name__ == '__main__':
	main()
