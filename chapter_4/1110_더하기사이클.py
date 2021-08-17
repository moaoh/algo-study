#! /usr/bin/python3

def	main():
	g = int(input())
	if g < 10:
		g *= 10
	n = g
	count = 0
	while True:
		i1 =  n % 10
		i2 = (n // 10 + n % 10) % 10
		n = 10 * i1 + i2
		count += 1
		if n == g:
			break
	print(count)

if __name__ == '__main__':
	main()
