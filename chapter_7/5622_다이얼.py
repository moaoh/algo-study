#! /usr/bin/python3

def	main():
	code = '22233344455566677778889999'
	s = list(map(ord, input()))
	time = len(s)
	for i in s:
		time += int(code[i - ord('A')])
	print(time)

if __name__ == '__main__':
	main()
