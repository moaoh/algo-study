#! /usr/bin/python3

def	main():
	i = int(input())
	for d in range(i):
		a, b = map(int, input().split())
		print(a + b)

if __name__ == '__main__':
	main()
