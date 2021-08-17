#! /usr/bin/python3

def	main():
	d = int(input())
	for i in range(1, 10):
		print('%d * %d = %d' % (d, i, d * i))

if __name__ == '__main__':
	main()
