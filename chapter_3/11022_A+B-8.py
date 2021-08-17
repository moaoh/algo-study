#! /usr/bin/python3

import sys

def	main():
	n = int(input())
	for i in range(n):
		a, b = map(int, sys.stdin.readline().rstrip().split())
		print('Case #%d: %d + %d = %d' %(i + 1, a, b, a + b))

if __name__ == '__main__':
	main()
