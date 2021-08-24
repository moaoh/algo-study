#! /usr/bin/python3

def	main():
	n = str(bin(int(input())))
	out = 0;
	for i in n:
		if i == '1':
			out += 1
	print(out)

if __name__ == '__main__':
	main()
