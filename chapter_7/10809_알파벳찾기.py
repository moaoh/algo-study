#! /usr/bin/python3

def	main():
	i = list(map(ord, input()))
	out = [-1 for i in range(ord('a'), ord('z') + 1)]
	pos = 0;
	for j in i:
		if out[j - ord('a')] == -1:
			out[j - ord('a')] = pos
		pos += 1

	for k in out:
		print(k, end = ' ')
	print()

if __name__ == '__main__':
	main()
