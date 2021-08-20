#! /usr/bin/python3

def	main():
	n = int(input())
	count = 0
	for i in range(1, n + 1):
		if i < 100:
			count += 1
		else:
			num = i
			while num >= 100:
				s_num = str(num)
				if int(s_num[0]) - int(s_num[1]) == int(s_num[1]) - int(s_num[2]):
					num = num // 10
				else:
					break
			if num < 100:
				count += 1
	return count
			

if __name__ == '__main__':
	print(main())
