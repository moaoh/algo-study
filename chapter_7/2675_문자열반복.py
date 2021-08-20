#! /usr/bin/python3

def	main():
	n = int(input())
	lst = [input() for i in range(n)]
	for i in lst:
		x, s = i.split()
		out = ''
		for j in s:
			out += j * int(x)
		print(out)

if __name__ == '__main__':
	main()
