#! /usr/bin/python3

code = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

def	main():
	count = 0
	s = input()
	for i in code:
		while i in s:
			count += s.count(i)
			s = s.replace(i, '.')
	s = s.replace('.', '')
	count += len(s)
	print(count)		
		

if __name__ == '__main__':
	main()
	
