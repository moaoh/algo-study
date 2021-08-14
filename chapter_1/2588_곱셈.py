#! /usr/bin/python3

def	main():
	dest = int(input())
	src = input()
	for i in list(map(lambda i: dest * int(i), src))[::-1]:
		print(i)
	print(dest * int (src))

if __name__ == '__main__':
	main()

