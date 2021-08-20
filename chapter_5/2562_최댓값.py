#! /usr/bin/python3

import sys

def	main():
	lst = [int(input()) for i in range(9)]
	max_value = lst[0]
	index = 0
	for key, value in enumerate(lst):
		if max_value < value:
			max_value = value
			index = key
	print(max_value)
	print(index + 1)

if __name__ == '__main__':
	main()
