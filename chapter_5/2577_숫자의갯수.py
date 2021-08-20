#! /usr/bin/python3

def	main():
	result = [0 for i in range(10)]
	a, b, c = [int(input()) for i in range(3)]
	total = a * b * c
	for i in str(total):
		result[int(i)] += 1
	for i in result:
		print(i)

if __name__ == '__main__':
	main()
