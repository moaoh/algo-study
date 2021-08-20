#! /usr/bin/python3

def	main():
	n = int(input())
	lst = list(map(int, input().split()))
	m = max(lst)
	lst = list(map(lambda x : x / m * 100, lst))
	av = 0.0
	for i in lst:
		av += i
	print(av / n)

if __name__ == '__main__':
	main()
