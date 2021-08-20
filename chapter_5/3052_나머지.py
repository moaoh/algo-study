#! /usr/bin/python3

def	main():
	out = [0 for n in range(42)]
	for n in range(10):
		i = int(input())
		out[i % 42] += 1
	count = 0;
	for i in out:
		if i > 0:
			count += 1
	print(count)

if __name__ == '__main__':
	main()

