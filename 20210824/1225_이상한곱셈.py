#! /usr/bin/python3

def	main():
	a, b = input().split()
	j = sum(list(map(int, b)))
	print(sum(map(lambda x: int(x) * j, a)))


if __name__ == '__main__':
	main()
