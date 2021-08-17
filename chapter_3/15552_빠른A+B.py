#! /usr/bin/python3

import sys

def	main():
	d = int(input())
	for i in range(d):
		j, k = map(int, sys.stdin.readline().rstrip().split())
		print(j + k)
	
if __name__ == '__main__':
	main()

