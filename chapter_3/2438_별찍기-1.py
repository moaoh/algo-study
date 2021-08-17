#! /usr/bin/python3
from functools import reduce

def	main():
	n = int(input())
	out = ''
	for i in range(n):
		out += '*'
		print(out)

if __name__ == '__main__':
	main()
