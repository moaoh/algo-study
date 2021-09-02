#! /usr/bin/python3

def	func_(a:int, b:int, i:int):
	if i <= 2:
		if i == 0:
			return 0
		else:
			return a + b
	return func_(b, a + b, i - 1)

def	main():
	n = int(input())
	print(func_(0, 1, n))


if __name__ == '__main__':
	main()
