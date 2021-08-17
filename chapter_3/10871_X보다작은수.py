#! /usr/bin/python3

def	main():
	leng, div = map(int, input().split())
	n = list(map(int, input().split()))
	for i in n:
		if i < div:
			if n.index(i) == leng - 1:
				print(i)
			else:
				print(i, end = ' ')

if __name__ == '__main__':
	main()
