#! /usr/bin/python3

def	main():
	n = int(input())
	lst = [int(input()) for _ in range(n)]
	out = 0
	lst.sort(reverse=True)
	for i, j in enumerate(lst):
		if j - i > 0:
			out += j - i
		else:
			break
	print(out)


if __name__ == '__main__':
	main()
