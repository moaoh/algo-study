#! /usr/bin/python3

def	main():
	n = int(input())
	lst = [input() for i in range(n)]

	for s in lst:
		add = 0
		total = 0
		for j in s:
			if j == 'O':
				add += 1
			else:
				add = 0
			total += add
		print(total)

if __name__ == '__main__':
	main()
