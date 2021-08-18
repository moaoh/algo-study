n = int(input())
for x in range(n):
	str = input()
	num = 0
	count = 1
	for s in str:
		if s == 'O':
			num += count
			count += 1
		else:
			count = 1
	print(num)