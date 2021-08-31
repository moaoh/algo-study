#! /usr/bin/python3

def	hanoy(num:int, from_:int, to_:int, lst:list):
	if num == 0:
		return 0
	tmp = 6 - from_ - to_
	a = hanoy(num - 1, from_, tmp, lst)
	lst += [(from_, to_)]
	b = hanoy(num - 1, tmp, to_, lst)
	return 1 + a + b

def	main():
	lst = []
	n = int(input())
	print(hanoy(n, 1, 3, lst))
	for i, j in lst:
		print(i, j)



if __name__ == '__main__':
	main()
