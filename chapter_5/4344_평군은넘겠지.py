#! /usr/bin/python3

from itertools import accumulate

def	main():
	n = int(input())
	lst = [list(map(int, input().split())) for i in range(n)]
	for i in lst:
		av = 0
		count = 0
		av = sum(i[1:]) / i[0]
		for j in i[1:]:
			if j > av:
				count += 1
		print('%.3f%%' % ((count / i[0]) * 100))

if __name__ == '__main__':
	main()
