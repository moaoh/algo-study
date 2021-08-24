def	number():
	n = input()
	if n != '0':
		l = len(n)
		for x in range(l // 2):
			if n[x] != n[l - 1 - x]:
				print("no")
				return number()
		print("yes")
		return number()
	return 0

number()