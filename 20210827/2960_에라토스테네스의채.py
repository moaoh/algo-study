#! /usr/bin/python3

def	main():
	i, j = map(int, input().split())
	lst = list(range(2, i + 1))
	count = 0
	while j > 0:
		l = lst[0]
		for k in lst:
			if k % l == 0:
				lst.remove(k)
				j -= 1
				if j == 0:
					print(k)
					break


if __name__ == '__main__':
	main()
