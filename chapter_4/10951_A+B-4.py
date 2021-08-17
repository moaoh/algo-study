#! /usr/bin/python3

def	main():
	try:
		while 1:
			a, b = map(int, input().split())
			print(a + b)
	except:
		return

if __name__ == '__main__':
	main()
