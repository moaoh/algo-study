#! /usr/bin/python3

def	main():
	n = int(input())
	lst = [input() for i in range(n)]
	count = 0
	for i in lst:
		dif = 0
		for j in range(ord('a'), ord('z') + 1):
			n = i.count(chr(j))
			if chr(j) * n not in i:
				diff = 1
		if dif == 0:
			count += 1
	print(count)

if __name__ == '__main__':
	main()
