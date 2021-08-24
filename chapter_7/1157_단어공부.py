#! /usr/bin/python3

def	main():
	s = input().upper()
	code = [0 for i in range(ord('A'), ord('Z') + 1)]
	for i in s:
		code[ord(i) - ord('A')] += 1
	if code.count(max(code)) > 1:
		print('?')
	else:
		print(chr(code.index(max(code)) + ord('A')))


if __name__ == '__main__':
	main()
