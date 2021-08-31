#! /usr/bin/python3

def	main():
	n = int(input())
	lst = [int(input()) for _ in range(n)]
	i = 1
	while i < n:
		num = lst[i]
		for key, value in enumerate(lst[0:i]):
			if value > num:
				del lst[i]
				lst.insert(key, num)
				break
		i += 1

	for i in lst:
		print(i)
			

if __name__ == '__main__':
	main()
