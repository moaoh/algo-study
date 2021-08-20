#! /usr/bin/python3

def	d(n):
	total = int(n)
	for i in str(n):
		total += int(i)
	return total

def	main():
	lst = [0 for i in range(10000)]
	n = 1
	while n < 10000:
		out = d(n)
		if out < 10000:
			lst[out] = 1
		n += 1
	n = 1
	while n < 10000:
		if lst[n] == 0:
			print(n)
		n += 1

if __name__ == '__main__':
	main()
