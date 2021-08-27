#! /usr/bin/python3 

import sys

def	chick(i:int, j:int):
	if i < j:
		return i
	return (i // j) * j + chick(i % j + i // j, j)

def	main():
		for i in sys.stdin.readlines():
			j, k = map(int, i.strip().split())
			print(chick(j, k))

if __name__ == '__main__':
	main()
