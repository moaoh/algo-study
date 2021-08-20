#! /usr/bin/python3

def	main():
	i = int(input())
	lst = list(map(int, input().split()))
	max_num, min_num = lst[0], lst[0]
	for n in lst[1:]:
		if n > max_num:
			max_num = n
		if min_num > n:
			min_num = n
	print(min_num, max_num)
#print(min(lst), max(lst))

if __name__ == '__main__':
	main()
