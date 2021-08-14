#! /usr/bin/python3

def	main():
	out = []
	result = 0;
	dest = input()
	src = input()
	for i in map(lambda i: int(dest) * int(i), src):
		out.insert(0, i)
	
	for i, value in enumerate(out):
		print(value)
		result += (10 ** i) * value
	print(result)


if __name__ == '__main__':
	main()

