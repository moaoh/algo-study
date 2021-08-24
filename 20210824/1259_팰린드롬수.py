#! /usr/bin/python3

def	main():
	lst = []
	while True:
		i = input()
		if i == '0':
			break ;
		lst.append(i)
	for i in lst:
		if i == i[-1::-1]:
			print('yes')
		else:
			print('no')


if __name__ == '__main__':
	main()
